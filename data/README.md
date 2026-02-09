# Title of Dataset
---

The experimental protocol was accredited by the Human Research Ethics Committee of Prince of Songkla University, Songkhla, Thailand (protocol number: 62-029-1-1, date of approval: 22nd July 2020). Forty healthy university students, including 21 females (18–25 years of age), were selected for this study. Written consents of the subjects were obtained. All subjects have no history of neurological or cardiovascular diseases and no history of using any medication that might affect the autonomic nervous system. The female subjects were asked to provide the date of the first day of their last period to determine the phase of the menstrual cycle that they were in on the recording day. After a rest period of 15 minutes, their blood pressure was measured. The Thai version of the Perceived Stress Scale (T-PSS-10) was used to measure underlying stress in the last 1 month before the experimental day from which a subject’s stress was classified into three levels. All 40 subjects taking part in this experiment had low or moderate stress scores and thus were included in the study. All experiments were conducted in the quiet laboratory conditions in the afternoon time (2–4 pm) to control the effect of circadian rhythms on physiological activity. 

The ECG was acquired using a bipolar limb lead (right arm-left leg) connected to ECG amplifier (ADinstruments, Dunedin, New Zealand).  The signals were band-pass filtered between 0.3-200 Hz and sampled at 1000Hz. EEG electrodes were placed using a cap with 8 electrodes: Fp1, Fp2, F3, F4, P3, P4, T3, and T4 according to the international 10-20 system. Monopolar recording was performed between the active electrode and the reference electrode (average mastoids). The sampling frequency was 2000 Hz, and low-pass filtering with 200 Hz cut-off frequency was applied. The impedance was kept at ? 10 k? (eego? 8 ANT neuro, Hengelo, Netherlands). 

Mental arithmetic task (MAT) which is widely used to induce brain activation and physiological stress response (cortisol levels, blood pressure, and escalated heart rate), was used to induce stress in this study. A within-subjects design in which all participants are exposed to both control and stress conditions is used in this experiment to help reduce errors associated with interindividual differences in physiological factors such as breathing rate, heart rate and blood pressure. The experiment protocol was performed in six steps (see Figure 1). Step 1 (Habituation): a brief introduction was given to the subjects to familiarize them with the experimental procedure. No EEG or ECG signal was recorded during this period. Step 2 (Eyes open: EO period, that is, non-stress condition or baseline): baseline EEG and ECG signals were measured for 5 minutes. Subjects were instructed to look at a fixation dot on the computer screen with minimal head and body movement. Step 3 (Arithmetic stress task 1: AC1 period, that is, low stress condition): The subjects performed mental arithmetic tasks presented on the computer screen, which involved the subtraction (-), addition (+), division (/), and multiplication (x) between four numbers in a quiet environment for 5 minutes. The subjects completed arithmetic problems presented one at a time. After a problem appeared on the screen, the subjects had 30 seconds to give the correct answer by using the mouse click as quickly as possible. Feedback (correct/incorrect) was provided immediately following each response.

The difficulty and time given to each arithmetic problem was set in a way that the subjects could not exceed an accuracy of 50% (as derived from pilot subjects). Step 4 (Break): subjects were allowed to relax for 2 minutes. Step 5 (Arithmetic stress task 2: AC2 period, that is, high stress condition): the subjects performed the same procedure as described in the third step but with the audio distraction which was human voice talking. The audio distraction was used to reduce cognition while in mental demand to augment distress [48] and to mimic the real work environment, which is typically interrupted by sensory demand (stress detection in working people). Step 6 (Recovery): the subjects were allowed to recover for 5 minutes. 

The ECG signals were further digital high-pass filtered at 1 Hz and were examined to exclude cardiac arrhythmias (bradycardia (tachycardia (HR > 100), premature contraction, heart rate (HR) < 60). Mean HR (beats per minute) and the following heart rate variability features were then extracted: RMSSD (ms), pNN50 (%), NN50 (beats), SDNN (ms), AVNN (ms), LF/HF Ratio, HF Norm (a.u.), LF Norm (a.u.), LF (0.04–0.15 Hz) (ms2), HF (0.15–0.4 Hz) (ms2) (LabChart Software, ADInstruments). EEG signals were further digital high-pass filtered at 1 Hz. The 50Hz power and corresponding harmonics were notch filtered using FIR filter with a +/- 1 Hz cutoff. The fast Fourier transform (FFT) was used to calculate EEG absolute power of 7 frequency bands: delta 0–4 Hz, theta 4–8 Hz, alpha (mu) 8–13 Hz, beta1 13–20 Hz, beta2 20–30 Hz, low gamma 30–60 Hz, and high gamma 60–100 Hz from the 8 electrode positions. Relative power was the ratio between absolute power of a frequency band and the total power. Additionally, the interhemispheric asymmetries of the absolute and relative power of alpha, beta1, and beta2 were also calculated by taking the difference between the amplitudes of the signals and then normalizing it to the sum of their amplitudes in 4 homologous electrode pairs: T3-T4 (temporal cortex), P3-P4 (parietal cortex), F3-F4 (frontal cortex), and Fp1-Fp2 (prefrontal cortex). In summary, EEG features used in this study consisted of 1) the absolute and relative power of 7 frequency bands * 8 electrode positions making up a total of 112 features; and 2) interhemispheric asymmetry of the absolute and relative power of 3 bands * 4 electrode pairs making up a total of 24 features. The total number of ECG features was 11 and EEG was 136 (147 in total). 



## Description of the data and file structure

Data for 147  ECG and EEG features are contained in 3 separate files: 
	1) ECG(EO, AC1, AC2).xlsx,
	2) EEG(EO, AC1, AC2).xlsx,
	3) Ratio of Alpha _ Beta Power.xlsx. 
Each file contains features from 40 subjects. The details of each file are as follows.


1) ECG(EO, AC1, AC2).xlsx
This file contains data for 11 ECG features for 40 subjects (21 females, 19 males) extracted from ECG signals recorded from the non-stress period (baseline, EO), low-stress period (AC1), and high-stress period (AC2). Sheets titled 'EO' contains data for the EO period, 'AC1' for the AC1 period, and 'AC2' for the AC2 period. 

Column A in each sheet shows subject number, B subject's gender, C-M data for 11 ECG features.

Abbreviation
Mean HR: mean heart rate
AVNN: average NN interval
SDNN: standard deviation of NN interval
NN50: the number of times that NN intervals are longer than 50 ms
pNN50: the proportion of NN50 divided by the total number of NN intervals
RMSSD: root mean square of successive RR interval differences (RMSSD)
LF: power in the LF band
LF Norm: normalized power in the LF band
HF: power in the HF band
HF Norm: normalized power in the HF band
LF/HF ratio: ratio between power in the LF band and power in the HF band



2) EEG(EO, AC1, AC2).xlsx
This file contains data for absolute EEG power features for 40 subjects (21 females, 19 males) extracted from EEG signals recorded from the non-stress period (baseline, EO), low-stress period (AC1), and high-stress period (AC2). Sheets titled 'Non Normalize' contain data for non-normalized absolute EEG power features, 'Normalized' for normalized absolute EEG power features.

In each sheet, column A shows periods where the data was acquired from, B subject number, C subject's gender, D-K absolute EEG power in delta band (1-4 Hz) of signals acquired from 8 electrodes (Fp1, Fp2, F3, F4, T3, T4, P3, P4), L-S theta band (4-8 Hz), T-AA alpha band (8-12 Hz), AB-AI beta1 band (12-20 Hz), AJ-AQ beta2 band (20-30 Hz), AR-AY gamma1 band (30-60 Hz), AZ-BG gamma2 band (60-100 Hz).

*Artifact was detected at 90 Hz for Subject 21.


3) Ratio of Alpha _ Beta Power.xlsx
This file contains data for relative EEG power features for 40 subjects (21 females, 19 males) extracted from EEG signals recorded from the non-stress period (baseline, EO), low-stress period (AC1), and high-stress period (AC2). Sheets titled 'Alpha' contain data for alpha band, 'Beta1' beta1 band, and 'Beta2' beta2 band.

In 'Alpha' sheet, column A shows subject number, B subject's gender, C-N ratio of non-normalized alpha power recorded during EO, AC1, and AC2 periods for 4 electrode pairs (Fp1-Fp2, F3-F4, T3-T4, and P3-P4), O-Z ratio of normalized alpha power recorded during EO, AC1, and AC2 periods for 4 electrode pairs (Fp1-Fp2, F3-F4, T3-T4, and P3-P4).

In 'Beta1' sheet, column A shows subject number, B subject's gender, C-N ratio of non-normalized beta1 power recorded during EO, AC1, and AC2 periods for 4 electrode pairs (Fp1-Fp2, F3-F4, T3-T4, and P3-P4), O-Z ratio of normalized beta1 power recorded during EO, AC1, and AC2 periods for 4 electrode pairs (Fp1-Fp2, F3-F4, T3-T4, and P3-P4)

In 'Beta2' sheet, column A shows subject number, B subject's gender, C-N ratio of non-normalized beta2 power recorded during EO, AC1, and AC2 periods for 4 electrode pairs (Fp1-Fp2, F3-F4, T3-T4, and P3-P4), O-Z ratio of normalized beta2 power recorded during EO, AC1, and AC2 periods for 4 electrode pairs (Fp1-Fp2, F3-F4, T3-T4, and P3-P4)

