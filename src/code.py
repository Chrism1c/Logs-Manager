import pandas as pd
import openpyxl

# import socket
# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)

def loadLogs(file_names, ext_in):
    """
    Function useful to load data from log files (CSV|XLS|XLSX) and transform them into pandas dataframes
    :param file_names: list of selected file names
    :param ext_in: string object of input files extension
    :return: a list of dataframes
    """
    if ext_in == 'csv':
        frames = [pd.read_csv(f, delimiter=',', index_col=False) for f in file_names]
    else:
        frames = [pd.read_excel(name, engine='openpyxl') for name in file_names]
        # frames = [x.parse(x.sheet_names[0], header=0, index_col=None) for x in excels]
    return frames


def getHeaders(frames):
    """
    Function useful to extract headers strings from dataframes to merge
    :param frames: list of 2 dataframes
    :return: a list of file 1 headers and a list of file 2 headers
    """
    return list(frames[0].columns), list(frames[1].columns)


def saveLogs(result, output_path, ext_out):
    """
    Function useful to export the output file as csv or xls/xlsx file extension
    :param result: dataframe object result of concatenation or merge
    :param output_path: output path string
    :param ext_out: string object of output file extension
    :return: none
    """
    if ext_out == 'csv':
        result.to_csv(output_path, index=False)
    else:
        result = result.dropna(how='all')
        print(result.dropna(how='all'))
        result.to_excel(output_path, header=True, index=False)


def mergeLogs(lkey, rkey, file_names, output_path, ext_in, ext_out):
    """
    Procedure useful to execute the merge between two log files using a key header name
    :param lkey: string object of the selected header to use as key in the first dataframe
    :param rkey: string object of the selected header to use as key in the second dataframe
    :param file_names: list of selected file names
    :param output_path: output path string
    :param ext_in: string object of input files extension
    :param ext_out: string object of output file extension
    :return: none
    """
    frames = loadLogs(file_names, ext_in)
    if ext_in == 'csv':
        result = frames[0].merge(frames[1], left_on=lkey, right_on=rkey)
    else:
        result = frames[0].merge(frames[1], left_on=lkey, right_on=rkey)
    saveLogs(result, output_path, ext_out)


def concateneteLogs(file_names, output_path, ext_in, ext_out):
    """
    Procedure useful to execute the concatenation of two or more log files
    :param file_names: list of selected file names
    :param output_path: output path string
    :param ext_in: string object of input files extension
    :param ext_out: string object of output file extension
    :return: none
    """
    if ext_in == 'csv':
        combined = pd.concat([pd.read_csv(f, delimiter=',', names=None, index_col=False) for f in file_names])
    else:
        frames = [pd.read_excel(name, engine='openpyxl') for name in file_names]
        # turn them into dataframes
        # frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]
        # delete the first row for all frames except the first

        # frames[1:] = [df[1:] for df in frames[1:]]

        combined = pd.concat(frames).dropna()

    if ext_out == 'csv':
        combined.to_csv(output_path, index=False)
    else:
        combined.to_excel(output_path, index=False)


def findExtension(fileName):
    """
    Function useful to define used file extension
    :param fileName: string object of the selected file
    :return: string object of the extension of the file
    """
    if fileName.find('.csv') != -1:
        return "csv"
    elif fileName.find('.xlsx') != -1:
        return "xlsx"
    else:
        return "xls"
