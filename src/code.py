import pandas as pd
import openpyxl


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
        result.to_excel(output_path, header=True, index=False)


def mergeLogs(how_merge, lkey, rkey, file_names, output_path, ext_in, ext_out):
    """
    Procedure useful to execute the merge between two log files using a key header name
    :param how_merge: string object to select the type of join to perform ['left', 'right', 'outer', 'inner']
    :param lkey: string object of the selected header to use as key in the first dataframe
    :param rkey: string object of the selected header to use as key in the second dataframe
    :param file_names: list of selected file names
    :param output_path: output path string
    :param ext_in: string object of input files extension
    :param ext_out: string object of output file extension
    :return: none
    """
    frames = loadLogs(file_names, ext_in)

    result = pd.merge(frames[0], frames[1], how=how_merge, left_on=lkey, right_on=rkey)
    saveLogs(result, output_path, ext_out)

    # TEST JOINS #

    # mergeTypes = ['left', 'right', 'outer', 'inner']
    # results = list()
    # for how_merge in mergeTypes:
    #     print('\nhow_merge: ', how_merge)
    #     result = pd.merge(frames[0], frames[1], how=how_merge, left_on=lkey, right_on=rkey)
    #     print(result)
    #     results.append(result)
    # print("0-1 ", results[0].equals(results[1]))
    # print("0-2 ", results[0].equals(results[2]))
    # print("0-3 ", results[0].equals(results[3]))
    # print("1-2 ", results[1].equals(results[2]))
    # print("1-3 ", results[1].equals(results[3]))
    # print("2-3 ", results[2].equals(results[3]))


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
