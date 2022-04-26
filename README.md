# Leuven Embedded Figures Test (L-EFT) in PsychoPy
This is a PsychoPy implementation of the [Leuven Embedded Figures Test (L-EFT)](https://peerj.com/articles/2862/), with Swedish instructions.

## Different versions
This project includes 3 PsychoPy experiments:
* 'left-outside-scanner' holds a version of the L-EFT that is meant to be run on a single-screen setup, where the participant is seated at the experiment computer.
* 'instruction-demo' holds an experiment that is meant to be used for demonstrating the task to participants, e.g. to prepare them for doing the test inside of an MR scanner.
    - This is a very minimal demo,. No automated feedback is given to the participant; instead, it's expected that the tester will be discussing what is the correct/incorrect response with the participant before the participant actually presses a key/button to proceed.
* 'left-in-scanner' holds a version of the L-EFT that is meant to be used in a two-screen setup and with an MR scanner, where the participant is lying in the scanner with a response button pad.
    - Here the experiment (after instructions finish) waits for a signal from the scanner, corresponding to pressing the '5' key.
    - The experiment expects the scanning room monitor to be configured (in e.g. Windows monitor settings) as the secondary screen.
    - It's assumed that the response button pad is configured so that pressing the 'left' button corresponds to hitting the '3' key on a keyboard, and the 'right' button corresponds to hitting the '1' key.

It is likely that you will need to change experiment configurations, especially with regard to what signal the 'left-in-scanner' version should be listening.

## Stimuli (in non-demo versions)
The original L-EFT stimuli can be found on [figshare](https://figshare.com/articles/dataset/Leuven_Embedded_Figures_Test_Target_Shapes/3807885).

## Translating the experiment
In PsychoPy, click the Text Components (e.g. in the routine 'instructions_part_one' there is a component 'text_instructions_part_one'. In the window that pops up, edit the 'Text' field. It's recommended that you copy and paste the Swedish text snippets into e.g. Google Translate as a start.

Additionally, you need to:
1. Open 'left-in-scanner.psyexp'.
2. Go to 'instructions_part_one'.
3. Open up the 'code' component.
4. In the 'Before experiment' tab, scroll down to where you find the following code and update it with your translations. (make sure to leave the apostrophes `''`).
```py
NOTFOUND_TXT = 'Formen fanns här. Tryck höger knapp.'
FOUND_TXT = 'Precis, formen fanns här. Tryck höger knapp.'
```

Once you've finished translating the experiment, save it ('Save current experiment file' in main window toolbar) and try running it again.

## Attribution
The Leuven Embedded Figures Test was developed by Lee de-Wit​​, Hanne Huygelier​, Ruth Van der Hallen, Rebecca Chamberlain and Johan Wagemans. This PsychoPy implementation, and the new stimuli, were developed by Lowe Wilsson.

The original set of L-EFT stimuli as well as all material here are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), meaning you are free to use and modify everything in this project, __provided that you include proper attribution__. You are required to cite this article:

> De-Wit, L., Huygelier, H., Van der Hallen, R., Chamberlain, R., & Wagemans, J. (2017). Developing the Leuven Embedded Figures Test (L-EFT): testing the stimulus features that influence embedding. PeerJ, 5, e2862.

Additionally, though it's not required you are very welcome to link to [this project's GitHub repository](https://github.com/anonzebra/psychopy-left) so that others can find it.
