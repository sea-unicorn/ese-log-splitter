import PySimpleGUI as sg
from os import path, makedirs

sg.theme("LightBlue3")

filename = False

layout = [  [sg.Text('Click Browse to select ESO Log file to split and press Split button.')],
            [sg.Text('Log file'), sg.Input(size=(56,1), enable_events=True,key="-LOGFILE-"), sg.FileBrowse(file_types=(("Log Files", "*.log"),))],
            [sg.Text('',size=(46,1),key = "-OUTPUT-")],
            [sg.ProgressBar(100, orientation='h', size=(46, 20), key='-PROGBAR-')],
            [sg.Output(size=(70,20))],
            [sg.Button('Split',size=(10,1))]
         ]

window = sg.Window('Seaunicorns ESO Log Splitter', layout,finalize=True)

try:
    if path.getsize("Splitlog.config") > 0:
        with open("Splitlog.config", 'r') as pathfile:
            for line in pathfile:
                filename = line
        window['-LOGFILE-'].update(filename)
        
except OSError as e:
    filename = False

while True:             
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
        
    if event == "-LOGFILE-":
        filename = values["-LOGFILE-"]
        with open("Splitlog.config", 'w') as pathfile:
            pathfile.write(filename)
        
    if event == "Split" and not filename:
        window['-OUTPUT-'].update("Please select ESO Log file to split first (>**)>")
        
    if event == "Split" and filename:
        if not path.exists('To upload'):
            makedirs('To upload')
        try:
            filesize = path.getsize(filename)
            window['-OUTPUT-'].update("I am working...")
            with open(filename, encoding='UTF-8') as fin:
                start_line = 'BEGIN_LOG'
                trial_line = 'ZONE_CHANGED'
                unit_line = 'UNIT_ADDED'
                trial_start_line = 'TRIAL_INIT'
                log_lines = ''
                trial = ''
                prev_trial = ''
                players = set()
                prev_players = set()
                trial_start_ind = 0
                n = 0
                fout = open("To upload\initial.log","wb")
                ln = 0
                for line in fin:       
                    ln+=1                    
                    if start_line in line:
                        
                        trial_start_ind = 0
                        if len(players) > 1:
                            prev_players = players
                            prev_trial = trial
                        players = set()
                        trial = ""
                        log_lines = line
                        
                    elif (trial_line in line)  & (trial_start_ind == 0):
                        trial = line.split(",")[3].strip('"')
                        log_lines += line
                        
                    elif (unit_line in line) & (trial_start_ind < 2):
                        trial_start_ind = 1
                        player = line.split(",")[11].strip('"')
                        players.add(player)
                        log_lines += line
                        
                    elif  (unit_line not in line) & (trial_start_ind == 1):
                        trial_start_ind = 2
                        
                        if ((len(prev_players.intersection(players)) < 6) or (prev_trial != trial)) and len(players) > 1:
                            n+=1
                            print ("\n ",n, trial,"\n")
                            print ("    -"+"\n    -".join(players))
                            progress = round(ln*17000/filesize)
                            window['-PROGBAR-'].update_bar(progress)  
                            if n > 1:
                                fout.close()
                            fout = open("To upload\%d %s.log"%(n,trial),"wb")
                        fout.write(log_lines.encode("utf-8"))

                    elif trial_start_ind == 2:    
                        fout.write(line.encode("utf-8"))
                    
                fout.close()            
            window['-OUTPUT-'].update("Yey, I have finished :3")
            window['-PROGBAR-'].update_bar(100)  
            print ("\n    You can find listed log files in the \"To upload\" directory.\n    Please do not forget to delete the original log file (**,)")
            
        except:
            window['-OUTPUT-'].update("Log file does not exist or something else went wrong :(") 

window.close()
