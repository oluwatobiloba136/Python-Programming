import json
from collections import defaultdict
from pathlib import Path

base_dir = Path(__file__).resolve().parent
input_path = base_dir / 'data' / 'view_dep_columns.json'
output_path = base_dir / 'data' / 'vw_erd.json'


def normalize_table_name(value):
    if value is None:
        return None
    cleaned = str(value).strip().replace('[', '').replace(']', '')
    if '.' in cleaned:
        cleaned = cleaned.split('.')[-1]
    return cleaned


def normalize_column_name(value):
    if value is None:
        return None
    return str(value).strip().replace('[', '').replace(']', '')


def normalize_source_object(value):
    if value is None:
        return None
    cleaned = str(value).strip().replace('[', '').replace(']', '')
    if '.' in cleaned:
        return cleaned
    return cleaned


with input_path.open('r', encoding='utf-8') as f:
    dependency_rows = json.load(f)

# Group tables by source view and track common columns used by the same view.
# A join is inferred when two tables in the same view reference the same column name.
view_table_columns = defaultdict(lambda: defaultdict(set))

for row in dependency_rows:
    source_object = row.get('SOURCE_OBJECT')
    table_name = normalize_table_name(row.get('REFERENCED_TABLE'))
    column_name = normalize_column_name(row.get('REFERENCED_COLUMN'))

    if not source_object or not table_name or not column_name:
        continue

    source_key = normalize_source_object(source_object)
    view_table_columns[source_key][table_name].add(column_name)

relationship_sources = defaultdict(set)

for source_key, table_map in view_table_columns.items():
    table_names = sorted(table_map.keys())

    for i in range(len(table_names)):
        for j in range(i + 1, len(table_names)):
            parent_table = table_names[i]
            child_table = table_names[j]
            shared_columns = table_map[parent_table] & table_map[child_table]

            if not shared_columns:
                continue

            join_column = sorted(shared_columns)[0]
            key = (parent_table, child_table, join_column)
            relationship_sources[key].add(source_key)

relationships = []
for (parent_table, child_table, join_column), source_objects in sorted(relationship_sources.items()):
    relationships.append({
        'parent_table': parent_table,
        'child_table': child_table,
        'join_type': 'INNER JOIN',
        'join_condition': f'{parent_table}.{join_column} = {child_table}.{join_column}',
        'source object': ', '.join(sorted(source_objects))
    })

# Keep the file narrow and specific to table join relationships only.
output = {
    'relationships': sorted(relationships, key=lambda x: (x['parent_table'], x['child_table'], x['join_condition']))
}

with output_path.open('w', encoding='utf-8') as f:
    json.dump(output, f, indent=4)

print(f'✓ Created {output_path}')
print(f'  - Total relationship rows: {len(output["relationships"])}')
print(f'  - Sample: {output["relationships"][:3]}')
