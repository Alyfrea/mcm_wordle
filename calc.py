from openpyxl import load_workbook, Workbook
from scipy.stats import norm

wb = load_workbook('question2.xlsx')
sh = wb['Sheet1']
nwb = Workbook()
nsh = nwb.active

nsh.append(['期望预测', '方差预测', '预测1', '预测2', '预测3', '预测4', '预测5', '预测6', '预测7'])
for ln, item in enumerate(sh.iter_rows(min_col=2, max_col=5, min_row=2, max_row=360), 2):
    tag1 = item[1].value
    tag2 = item[3].value
    tag3 = item[2].value
    tag4 = item[0].value
    exe = 4.596 - 0.001 * tag1 + 0.348 * tag2 - 0.002 * tag3 - 0.001 * tag4
    exs = 1.027 + 0.003 * tag1 - 0.049 * tag2 + 0.0 * tag3 + 0.001 * tag4
    val = norm.pdf([1, 2, 3, 4, 5, 6, 7], loc=exe, scale=exs)
    val /= val.sum()
    val *= 100
    nsh.append([exe, exs, *val])
nwb.save('./question2_res.xlsx')
