import os
import inspect


def get_path_to_urdf_file(robot_name):
    module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    urdf_dir = os.path.join(module_dir, "description", "urdf")
    urdf_file_path = os.path.join(urdf_dir, robot_name + ".urdf")

    if os.path.isfile(urdf_file_path):
        return urdf_file_path
    else:
        # get list of available robot names
        f = []
        for (_, _, filenames) in os.walk(urdf_dir):
            f.extend(filenames)
            break
        valid_robot_names = []
        for j in range(len(f)):
            if f[j].endswith(".urdf"):
                valid_robot_names.append(os.path.splitext(f[j])[0])
        raise ValueError("No urdf file found for robot_name='{}'. "
                         "Valid values for robot_name are {}".format(robot_name, valid_robot_names))



