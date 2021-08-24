# URDF Files for Humanoid Robots of the ARMAR Family

This repository provides (unofficial) URDF files for some of the humanoid robots of the ARMAR family.

## Supported Robots

As of now, the following robots are supported:
<table width="100%">
    <thead>
        <tr>
            <th></th>
            <th>robot_name</th>
            <th>DOF</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=2 style="text-align:center"><img src="https://user-images.githubusercontent.com/51738372/130495206-be360e87-2444-4481-86eb-44df5c949880.png" width="100%"></td>
            <td>armar6</td>
            <td>17</td>
            <td>The humanoid robot Armar 6 with a fixed head and rigid hands.</td>
        </tr>
        <tr>
            <td>armar6_front</td>
            <td>17</td>
            <td>Like armar6, but the position of continuous joints is restricted such that the hands are mostly in front of the robot. </td>
        </tr>
        <tr>
            <td rowspan=2 style="text-align:center"><img src="https://user-images.githubusercontent.com/51738372/130494311-0c5e0265-30fc-4a54-962d-a853f16d7cbc.png" width="100%"></td>
            <td>armar6_x4</td>
            <td>33</td>
            <td>A four-armed version of Armar 6 with a fixed head and rigid hands.</td>
        </tr>
        <tr>
            <td>armar6_x4_front</td>
            <td>33</td>
            <td>Like armar6_x4, but the position of continuous joints is restricted such that the hands are mostly in front of the robot. </td>
        </tr>
    </tbody>
</table>


The corresponding URDF files can be found in the [description directory](https://github.com/translearn/armar-urdf/tree/main/armar/description). 
As shown below, it is also possible to access the models directly from python. 


## Installation

    pip install armar


## Usage
The following example shows how to receive the absolute path of a URDF file from python:

```python
import armar
armar.get_path_to_urdf_file(robot_name="armar6")
```

## Example: Models controlled by a Neural Network

[![Video: 2 vs. 4 Arms: Humanoid Battle controlled by Neural Networks](https://yt-embed.herokuapp.com/embed?v=Iib3wC0O5no)](https://www.youtube.com/watch?v=Iib3wC0O5no)




## Acknowledgment and Disclaimer

The robots of the ARMAR family are designed and developed by the [Chair of High Performance Humanoid Technologies (H²T)](https://h2t.anthropomatik.kit.edu/english/index.php) at the Karlsruhe Institute of Technology (KIT).
The URDF files provided in this repository are based on models provided by the Chair of High Performance Humanoid Technologies.
The four-armed version of Armar 6 is not an official part of the ARMAR family developed at H²T.


## License

The files of this repository are licensed under the [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/) license. 


 

