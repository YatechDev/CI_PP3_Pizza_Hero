import time

title_art = '''
                                                ██████  ██ ███████ ███████  █████      ██   ██ ███████ ██████   ██████                                   
                                                ██   ██ ██    ███     ███  ██   ██     ██   ██ ██      ██   ██ ██    ██  ██                             
                                                ██████  ██   ███     ███   ███████     ███████ █████   ██████  ██    ██      
                                                ██      ██  ███     ███    ██   ██     ██   ██ ██      ██   ██ ██    ██  ██                                
                                                ██      ██ ███████ ███████ ██   ██     ██   ██ ███████ ██   ██  ██████                                       
            
            ████████ ██   ██ ███████     ███    ███ ██    ██ ███████ ██   ██ ██████   ██████   ██████  ███    ███      ██████  ██    ██ ███████ ███████ ████████ 
               ██    ██   ██ ██          ████  ████ ██    ██ ██      ██   ██ ██   ██ ██    ██ ██    ██ ████  ████     ██    ██ ██    ██ ██      ██         ██    
               ██    ███████ █████       ██ ████ ██ ██    ██ ███████ ███████ ██████  ██    ██ ██    ██ ██ ████ ██     ██    ██ ██    ██ █████   ███████    ██    
               ██    ██   ██ ██          ██  ██  ██ ██    ██      ██ ██   ██ ██   ██ ██    ██ ██    ██ ██  ██  ██     ██ ▄▄ ██ ██    ██ ██           ██    ██    
               ██    ██   ██ ███████     ██      ██  ██████  ███████ ██   ██ ██   ██  ██████   ██████  ██      ██      ██████   ██████  ███████ ███████    ██    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                           

'''

pizza_art = '''

                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
                    ⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇          Just one more slice before we go...
                    ⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
                    ⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀
                    ⠀⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀
                    ⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠈⠓⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

game_over_art = '''

                                        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                                        ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                                        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                                        ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                                        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                                        ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                                        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                                        ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                                        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                                        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                                        ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                                        ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                                        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
                                        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

game_completed_art = '''

                                             ⡀⢠⡠⣄⢠⡂⠺⠁⠫⠭⠂⠉⠉⠧⠰⢀⠤⡤⣀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠁⡐⠈⠚⠑⠃⠀⠀⢠⣴⣆⠀⠄⣠⢶⠐⣑⠤⠨⡐⠀⣉⠟⢓⠢⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠴⠾⡿⠁⠀⠀⠑⢰⣶⢾⡽⣛⡯⠟⢢⠛⡐⣈⠌⠃⠍⢁⢈⠜⣀⠥⠅⡝⠔⠁⠘⡩⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⢑⢀⠔⠑⢘⠃⡞⠥⢢⣾⣿⣾⣿⢿⣭⡙⠞⠓⡐⠊⠌⣥⣾⣾⣷⣷⣿⡖⢸⠘⠰⡄⣀⠓⠤⡙⠱⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⡀⢊⠔⠂⠠⢂⣠⡾⡀⠋⠾⡭⢷⣿⣿⣿⣿⣿⣿⢿⡄⡄⡱⠠⣵⣿⣿⣿⣿⣟⣿⣷⡀⢀⡀⣸⢀⢄⠀⡁⣡⡄⡉⠅⡀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⢀⠊⢀⠠⣄⠤⣹⡿⢟⣾⣯⣄⣨⠂⠸⣿⣿⣿⢿⢿⣻⣿⠟⠠⠁⠀⣿⣿⣿⣟⣿⡽⣟⣿⢠⢀⠅⢀⠔⠋⢰⢸⡵⠴⣉⡄⠋⢆⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢠⡆⢀⡎⠺⡨⣓⢋⣾⣿⣿⣿⣿⣿⣯⠀⡙⠛⢿⣿⣾⠾⠋⠂⢓⠤⡀⠀⠻⢿⡿⣿⠿⠯⠋⠂⠌⣴⣾⣿⣿⣷⣾⡈⠐⠺⢿⡀⡀⠁⠀⠀⠀⠀⠀
                            ⠀⠀⠀⡒⢐⠄⠂⢋⢑⡀⢿⣿⣿⣿⣽⣾⣻⣿⡂⠎⠂⣀⠂⠄⢂⠤⣴⣶⣶⣶⣤⡀⢄⠀⠄⠢⢠⠀⠀⢯⣿⣿⣿⣟⡿⣿⣿⣜⣮⠈⣿⢞⠐⣱⡀⠀⠀⠀
                            ⠀⠀⠋⢂⠊⣠⡔⢜⠐⢠⠊⢿⣿⣿⣿⣿⣿⠟⠁⠀⠠⠰⢅⢎⠒⣾⣿⣿⢯⢿⣿⣷⣾⠠⢊⢕⡉⠀⢈⠼⣿⣿⣿⣿⢿⣿⣿⠟⠷⠭⠁⣿⣤⠀⣷⠀⠀⠀
                            ⠀⣾⡘⢣⡤⡝⠉⢀⢀⡌⡑⡈⠙⠓⠻⠋⠁⣀⣴⣶⣤⣄⢀⠠⠃⣿⣿⣟⣿⣯⣿⣯⡇⠀⠀⠈⢰⡡⠊⠇⠘⠿⣽⣯⠟⠟⡁⣂⠱⢸⠂⠈⠉⢱⢎⠡⠀⠀
                            ⠀⡏⠀⠐⣾⢰⣳⢿⣿⣿⣿⣧⣔⠢⣠⠚⣸⣿⣯⣿⣿⣿⣧⡁⡈⠈⠻⣿⣾⣯⡟⠋⠀⡄⣠⣾⣿⣿⣿⣷⣆⠀⡑⠁⡡⡄⠉⠠⡐⡈⣦⣀⠀⣯⡇⢎⡄⠀
                            ⣸⢃⠊⢼⡗⣸⣷⣿⣿⣿⣿⣿⣧⢚⠐⠀⢻⣿⣿⣻⣽⣿⣻⠀⠀⡀⠔⢂⠡⠃⠀⠀⣤⠑⣾⣟⣷⣿⣻⣿⣿⡇⠀⠈⡗⣰⣐⣀⣤⡉⣼⡋⢅⣛⣂⠠⢳⠀
                            ⡟⡄⠀⢻⠦⠙⣿⣿⣿⣞⣿⣿⡟⠀⠅⢄⠄⠋⠽⠽⠿⠋⠁⡀⢨⣾⣶⣶⣶⣷⣄⠄⢈⠈⢿⣯⣿⣏⣿⣿⣿⢆⢀⣣⣿⣿⣿⣿⣿⣿⣦⠨⡀⢈⡉⠇⢻⡀
                            ⡏⠄⣴⡻⢙⢤⣛⠿⠿⠿⠻⡉⡐⡲⠸⢀⣴⣷⣶⣄⠄⠀⠈⢲⣿⣿⣿⣿⣿⣾⣿⡆⠀⢐⡕⠃⢻⠿⠿⠛⡁⠀⠀⢻⣿⣿⣿⣿⣿⣻⣿⡄⠁⣴⡟⡵⢠⠀
                            ⡗⠂⡹⡷⡌⠨⠽⣠⣐⡀⠐⠅⠑⠑⣴⣾⣿⣿⢿⣿⣦⡀⠀⠘⣿⣿⣿⣿⣿⣿⡿⢇⣀⢨⠑⠠⡪⠄⣦⣴⣥⣴⡀⠚⣿⣿⣽⣯⣿⣿⡟⢁⣀⠙⠁⡁⠮⠀
                            ⣷⠄⢘⡷⣰⣾⣿⣿⣿⣿⣿⣆⣀⠴⣿⣿⣿⡿⣿⣿⣿⣷⠂⡀⠹⢿⣿⡾⣿⡷⠟⠀⠂⡁⣤⡆⠇⣾⣿⡿⣿⣿⣿⣆⠉⠛⠻⢯⠟⠉⠀⠅⢊⡀⣖⢹⣼⠆
                            ⢿⠣⡀⣽⡷⣿⣿⣿⣿⣿⠿⣿⣇⢂⡻⣿⣿⣟⣿⣿⡿⠋⠀⠁⠀⡀⢈⠝⣋⣤⣶⣶⣶⣬⡻⢇⠀⣿⣟⣿⢿⣾⣿⡏⠀⠎⡓⠅⢣⡪⠀⣠⡛⣽⡟⡆⢸⠀
                            ⠘⡧⢠⣗⣽⢿⣿⣿⣿⣿⣿⣿⠇⠈⠁⡌⠻⡛⠛⠩⢆⣡⣄⢤⢀⠢⠂⢠⣿⣿⡿⣿⣿⣻⣷⣦⠂⡈⠻⢿⠿⠿⢪⣡⣶⣾⣥⣆⠀⠀⠮⠼⣿⣿⢿⡩⠓⠀
                            ⠀⠹⡀⢻⣿⣆⠟⠻⠿⠿⢛⡁⣠⣫⣀⣔⣌⠲⠀⢠⣾⣿⢻⣿⢿⣷⡜⢸⣿⣿⣿⣾⣿⣿⣿⢃⠌⠠⠋⠥⠓⢠⣾⢿⣹⣿⣿⣿⣷⡀⠰⢾⡤⣝⠂⣠⠁⠀
                            ⠀⠀⢓⠇⡻⢿⡼⢀⠨⣀⡔⣡⣿⣻⣿⣿⣿⣄⡋⢹⣿⣿⣿⣿⢾⣿⡂⠌⠛⣿⣿⣿⣳⠗⡩⢆⠟⠘⠔⠠⣈⢸⣿⣿⣿⣿⣿⣿⣿⣙⣫⣿⣏⠁⠀⠇⠀⠀
                            ⠀⠀⠀⢧⠌⢐⡙⢆⣊⣏⢈⣿⣿⣿⡿⣽⣝⣿⠅⡨⠻⢿⣿⡾⠿⠋⢀⡀⡽⣭⢱⠹⣊⢞⣄⣴⣶⣶⣶⣥⡈⠈⠻⣿⣿⣿⣿⣿⢋⣾⠶⡃⢛⢉⡐⠀⠀⠀
                            ⠀⠀⠀⠈⢻⣄⠒⡼⣣⡶⣦⢿⣿⣿⣿⣿⣿⡟⠙⣡⡢⡀⢀⢤⣴⣾⣿⣿⣿⣾⣥⡔⠤⢫⣿⣿⣿⣿⣿⣿⣷⣀⠑⡀⣍⠿⣻⠶⠟⠁⠀⣀⢊⠈⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠙⢿⣌⢣⠄⠀⠙⢿⣛⢙⠛⠡⠀⠚⡂⢷⣶⠞⢹⣿⣿⣿⣻⣿⢟⣿⢤⠐⠸⣿⣿⣾⣻⣿⣽⣿⣃⣵⠚⠈⡌⠀⠀⠴⠀⠞⡀⠊⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠙⢷⣌⢢⡈⠹⠇⢔⡼⣇⡄⠄⠊⠁⣂⡂⢸⣿⣿⣻⣿⣽⣿⣿⣣⠠⠀⠙⢷⣿⡿⣿⡿⣟⣿⣅⠂⠈⢠⣶⣠⡄⢰⠋⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣦⣴⢀⢨⠹⡛⢮⠽⢶⡌⢀⢀⠒⠈⢛⠻⡿⠿⢏⣙⠻⣾⠀⣤⣆⡆⣤⣄⠺⢝⡛⢊⠀⠀⠀⠋⡱⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠛⢷⣗⡂⠉⠾⢇⣧⡽⣧⢍⣨⠔⢩⢽⡖⢫⣝⡌⣦⠈⡽⡛⠻⠻⢙⡙⠉⢀⣄⠡⠔⡡⠄⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠣⢦⣪⡉⠪⠯⠜⠻⢖⣿⣿⠆⠈⠓⠀⠀⠛⢌⠁⢀⣀⢀⠔⣠⡿⠌⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠴⠶⠤⠦⠤⠔⠀⢤⡴⡄⠤⠆⠑⠊⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''