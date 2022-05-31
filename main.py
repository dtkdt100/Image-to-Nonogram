import image_utils as iu
import numpy as np

image_path = "examples/test1.png"
save_path = "examples/result1.jpeg"
divided_size_by = 20


def generate_numerical_from_boolean(numpy_boolean_array):
    """
    Generates a list of lists of 0 and 1 from a numpy boolean array
    """
    return numpy_boolean_array.astype(int).tolist()


def generate_2D_list(numerical_list):
    """
    Generates a 2 dimensional list of the count of the number 0 in numerical_list.
    For example: numerical_list = [[1, 0, 0, 1], [0, 1, 0, 1]]
    returns: [[2], [1, 1]]
    """
    count_list = []
    for i in range(len(numerical_list)):
        count_list.append([])
        append_index = 0
        for j in range(len(numerical_list[i])):
            if numerical_list[i][j] == 0:
                if append_index >= len(count_list[i]):
                    count_list[i].append(1)
                else:
                    count_list[i][append_index] += 1
            else:
                if not append_index >= len(count_list[i]):
                    append_index += 1

    return count_list


def generate_Xlist(numpy_boolean_array):
    img_data_x = generate_2D_list(generate_numerical_from_boolean(numpy_boolean_array))
    return img_data_x


def fix_list(list_to_fix, insert_additional_times=0):
    """
    find the max len of lists in list_to_fix and then insert spaces to make all lists the same length
    """
    max_length = len(max(list_to_fix, key=len))+insert_additional_times
    for i in range(len(list_to_fix)):
        if len(list_to_fix[i]) < max_length:
            for j in range(max_length - len(list_to_fix[i])):
                list_to_fix[i].insert(0, " ")
    return list_to_fix


def swap_rows_and_columns(two_dimensional_list):
    return np.array(two_dimensional_list).T.tolist()


def generate_Ylist(numpy_boolean_array, max_len_x):
    img_data_y = swap_rows_and_columns(numpy_boolean_array)
    img_data_y = generate_2D_list(img_data_y)
    fix_list(img_data_y)
    img_data_y = swap_rows_and_columns(img_data_y)
    fix_list(img_data_y, max_len_x)
    return img_data_y


if __name__ == "__main__":
    img_data = iu.generate_img_for_nonogram(image_path, divided_size_by, show_stages=True)
    x_list = generate_Xlist(img_data)
    max_len_x = len(max(x_list, key=len))
    y_list = generate_Ylist(img_data, max_len_x)
    fix_list(x_list)
    iu.two_dim_to_nonogram(x_list, y_list, save_path)
