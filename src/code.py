import pandas as pd


# import socket
# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)

def loadLogs(file_names, ext_in):
    if ext_in == 'csv':
        frames = [pd.read_csv(f, delimiter=';', index_col=False) for f in file_names]
    else:
        excels = [pd.ExcelFile(name) for name in file_names]
        frames = [x.parse(x.sheet_names[0], header=0, index_col=None) for x in excels]
    return frames


def getHeaders(frames):
    return list(frames[0].columns), list(frames[1].columns)


def saveLogs(reult, output_path, ext_out):
    if ext_out == 'csv':
        reult.to_csv(output_path, index=False)
    else:
        reult.to_excel(output_path, header=True, index=False)


def mergeLogs(lkey, rkey, file_names, output_path, ext_in, ext_out):
    frames = loadLogs(file_names, ext_in)
    if ext_in == 'csv':
        reult = frames[0].merge(frames[1], left_on=lkey, right_on=rkey)
    else:
        reult = frames[0].merge(frames[1], left_on=lkey, right_on=rkey)
    saveLogs(reult, output_path, ext_out)


def concateneteLogs(file_names, output_path, ext_in, ext_out):
    if ext_in == 'csv':
        combined = pd.concat([pd.read_csv(f, delimiter=';', names=None, index_col=False) for f in file_names])
    else:
        excels = [pd.ExcelFile(name) for name in file_names]
        # turn them into dataframes
        frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]
        # delete the first row for all frames except the first
        frames[1:] = [df[1:] for df in frames[1:]]
        combined = pd.concat(frames)
    if ext_out == 'csv':
        combined.to_csv(output_path, index=False)
    else:
        combined.to_excel(output_path, header=False, index=False)


def findExtension(fileName):
    if fileName.find('.csv') != -1:
        return "csv"
    elif fileName.find('.xlsx') != -1:
        return "xlsx"
    else:
        return "xls"

# def mergeLogs(lkey, rkey, file_names, output_path, ext_in, ext_out):
#     if ext_in == 'csv':
#         frames = [pd.read_csv(f, delimiter=';', index_col=False) for f in file_names]
#         output = frames[0].merge(frames[1], left_on=lkey, right_on=rkey)
#     else:
#         excels = [pd.ExcelFile(name) for name in file_names]
#         # turn them into dataframes
#         frames = [x.parse(x.sheet_names[0], header=0, index_col=None) for x in excels]
#         output = frames[0].merge(frames[1], left_on=lkey, right_on=rkey)
#     if ext_out == 'csv':
#         output.to_csv(output_path, index=False)
#     else:
#         output.to_excel(output_path, header=True, index=False)
