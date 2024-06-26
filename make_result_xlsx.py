import pandas as pd
from glob import glob
import json

def _get_metric_name(v):
    metrics = ['f1', 'macro_f1', 'acc_norm', 'acc']
    for m in metrics:
        if v.get(m):
            return {
                'metric': m,
                'value': v[m],
            }

def get_shot_scores(path, shot_count):
    shot = f'{path}/{shot_count}_shot.json'
    try:
        results = json.load(open(shot))['results']
        return {f"{k} ({_get_metric_name(v)['metric']})": _get_metric_name(v)['value'] for k, v in results.items()}
    except FileNotFoundError:
        return {}

def create_shot_df(various_models, shot_count):
    data = {}
    for model in various_models:
        model_name = model.split('/')[-1]
        data[model_name] = get_shot_scores(model, shot_count)
    
    df = pd.DataFrame(data).T
    return df

various_models = sorted(glob('results/all/*/*'))

# Create dataframes for each shot count
df_0_shot = create_shot_df(various_models, 0)
df_5_shot = create_shot_df(various_models, 5)
df_10_shot = create_shot_df(various_models, 10)

# Save to Excel with multiple sheets
with pd.ExcelWriter('model_shots.xlsx') as writer:
    df_0_shot.to_excel(writer, sheet_name='0-shot')
    df_5_shot.to_excel(writer, sheet_name='5-shot')
    df_10_shot.to_excel(writer, sheet_name='10-shot')

print("Excel file created successfully with 0-shot, 5-shot, and 10-shot sheets.")

