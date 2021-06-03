<!-- PROJECT LOGO -->
<br />
<p align="center">
<img src="https://raw.githubusercontent.com/m3bolt/MarkerMixer/main/GIthub%20Resources/PMP%20Logo.png" alt="drawing" width="300"/>

  <p align="center">
   Marker mixer/blender for dying filament with permanent markers before it enters the hotend
    <br />
	<a href="https://discord.gg/TchtRx5vXf"><strong>Join the PMP Discord </strong></a>
	·
    <a href="https://github.com/m3bolt/MarkerMixer/tree/main/STLs"><strong>Download STLs </strong></a>
	·
    <a href="https://www.youtube.com/watch?v=Sshl-3-f8Ro"><strong>PMP Demo Video </strong></a>
    ·
    <a href="https://github.com/m3bolt/MarkerMixer/issues">Report Bug</a>
    ·
    <a href="https://github.com/m3bolt/MarkerMixer/issues">Request Feature</a>
  </p>
</p>






<!-- ABOUT THE PROJECT -->
## About The Project

The Poor Mans Palette is designed to use servos to slide markers in out and of a central filament path. It is an evolution of and directly inspired by Youtuber Makers Muse who designed a manual version.


<!-- GETTING STARTED -->
## Getting Started

Using the Poor Mans Palette is easy, but it does require some setup. <a href="https://github.com/kackle1998">Viperian</a> has created <a href="https://docs.google.com/document/d/1HtXDXiIX8TrwlF5AgzMKKhFVkw75yK6E26BhG-3SkN0/edit"><strong>Google Doc Instructions</strong></a> for new users to set up and use their PMP. 

You will need some electronics and hardware:

| Part Name | Description | Quantity |
| ------------- | ------------- | ------------- |
| 3D Printer running Klipper | Klipper is required for servo control | 1 |
| Arduino (Nano or Uno)  | Used by Klipper to address servo pins  | 1 |
| 5v 1A+ Power Supply | Necessary to power servos, barrel jack recommended | 1 |
| M3 x 10mm screw | To secure Marker Holder to Marker Hub | 6 |
| M3 x 12mm screw | To hold the marker in in the Marker Slider | 3 |
| M3 Locknut | To secure Marker Screw Cap to 12mm screw | 3 | 
| M3 x 16mm screw | To mount Marker Hub to your printers Hub Mount | 3 |
| Breadboard or Perfboard | Used for wiring servos to the Arduino | 1 |
| 3-pin DUPONT headers | For plugging the servos into your breadboard or perfboard | 3 |
| SG90 Servo Motor | Used to extend and retract the markers | 3 |
| SG90 Servo mounting screws | Usually included with your SG90, these secure the servo to the Marker Body | 6 |

The following are the STLs required for a 3 marker setup and the quantity of each required: 

| Part Name | Notes | Quantity |
| ------------- | ------------- | ------------- |
| PMP_MarkerHub_R1.stl | | 1 |
| PMP_MarkerBody_NumX_R1.stl | Requires supports! Print NoNum for no numbers or 1-3 for numbered versions. | 3 |
| PMP_MarkerSlider_Size_ID_R1.stl | 2 versions available, one with a smaller ID and one with a larger ID. Print one at a time to verify the size required! | 3 |
| PMP_ServoGear_Size_ID_R1.stl | 5 versions available with different IDs for the servo shaft. Print one at a time to verify the size required! | 3 |
| PMP_MarkerScrewCap_R1.stl | Optional thumb screw caps for the set screw holding the marker in the slider | 3 |

Hub mounts to follow for some machines. 

In theory you can stack PMPs on top of eachother for even more color combinations and options, but we recommend starting with one set of 3. 

<!-- CONTACT -->
## Contact

If you need help or want to reach out, message Viperian and M3 Bolt on our 	<a href="https://discord.gg/TchtRx5vXf">Discord server.</a>

Project Link: https://github.com/m3bolt/MarkerMixer

<!-- LICENSE -->
## License

Distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license.


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* <a href="https://github.com/kackle1998">Viperian,</a> who originally had the idea of automatic slicer controlled marker switching and did all of the software/slicer parts of the project.
* <a href="https://www.youtube.com/channel/UCxQbYGpbdrh-b2ND-AfIybg">Makers Muse,</a> who showed a video of a manual marker filament dying system that inspired the project.
* <a href="https://github.com/m3bolt">M3 Bolt,</a> who did most of the Fusion based CAD work for the project.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
