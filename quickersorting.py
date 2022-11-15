import shutil
import fnmatch
import os
import pathlib

Path1 = "C:/Users/Flynn/Documents/GitHub/Adag.io/"
DPath = "C:/Users/Flynn/Documents/GitHub/Adag.io/dataset/"

original_folder = 'dataset_by_instrument/real guitar eshape/'

endfolders = ["A Major","A# Major","B Major","C Major","C# Major",
              "D Major","D# Major","E Major","F Major","F# Major",
              "G Major","G# Major",
              "A Minor","A# Minor","B Minor","C Minor","C# Minor",
              "D Minor","D# Minor","E Minor","F Minor","F# Minor",
              "G Minor","G# Minor",
              "A Major7", "A# Major7", "B Major7", "C Major7", "C# Major7",
              "D Major7", "D# Major7", "E Major7", "F Major7", "F# Major7",
              "G Major7", "G# Major7",
              "A Minor7", "A# Minor7", "B Minor7", "C Minor7", "C# Minor7",
              "D Minor7", "D# Minor7", "E Minor7", "F Minor7", "F# Minor7",
              "G Minor7", "G# Minor7"
              ]
data_dir = pathlib.Path(original_folder)
for file in os.listdir(original_folder):
    if fnmatch.fnmatch(file, '01*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[0] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '02*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[1] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '03*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[2] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '04*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[3] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '05*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[4] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '06*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[5] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '07*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[6] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '08*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[7] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '09*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[8] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '10*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[9] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '11*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[10] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '12*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[11] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
####################### end of major ###############################
    if fnmatch.fnmatch(file, '14*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[12] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '15*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[13] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '16*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[14] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '17*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[15] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '18*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[16] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '19*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[17] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '20*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[18] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '21*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[19] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '22*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[20] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '23*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[21] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '24*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[22] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '25*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[23] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    ########################## end minor  ##########################
    if fnmatch.fnmatch(file, '27*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[24] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '28*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[25] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '29*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[26] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '30*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[27] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '31*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[28] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '32*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[29] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '33*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[30] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '34*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[31] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '35*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[32] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '36*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[33] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '37*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[34] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '38*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[35] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
########################## end of maj7 ##################################
    if fnmatch.fnmatch(file, '40*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[36] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '41*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[37] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '42*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[38] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '43*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[39] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '44*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[40] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '45*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[41] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '46*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[42] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '47*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[43] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '48*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[44] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '49*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[45] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '50*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[46] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
    if fnmatch.fnmatch(file, '51*'):
        source = Path1 + original_folder + file
        destination = DPath + endfolders[47] + "/" + file
        shutil.move(source, destination)
        print('Moved:', file)
####################### end of min 7 #########################



