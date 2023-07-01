
from wonderwords import RandomWord, RandomSentence
import time

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QDialog, QMessageBox
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import QTimer
import logging
from typing import List


class SpeedTyper(QMainWindow):
    def __init__(self):
            super().__init__()
            
            self.setWindowTitle('Typing Speed Test') #Title
            
                       

            random_sentence = RandomSentence()
            random_list = [random_sentence := random_sentence.simple_sentence() for i in range(1) ] #generating random-sentence
            sentence: str = ''.join(random_list) #random Sentence
            normal_font = QFont('Times', 14)

            '''
            
            Header Label
            '''

            self.header = QLabel('Typing Speed Test',self) #Header
            self.header.setGeometry(0, 0, 240, 120)
            self.header.move(390,-42)
            self.header.setStyleSheet(
                    "font-family: Tahoma, sans-serif;"
                    "font-size: 20px;"
            )

            '''
            
            WPM Label for showing the WPM 
            '''

            self.wpm = QLabel('WPM   ',self)
            self.wpm.setFont(normal_font)
            self.wpm.setGeometry(0, 0, 240, 120)
            self.wpm.move(390,60)
            

            self.score_label = QLabel('Score:',self)
            self.score_label.setGeometry(0, 0,  440, 220)
            self.score_label.move(380,90)
            self.score_label.setStyleSheet(
                  "font-family: 'Times New Roman', Times, serif;"
                  "font-size: 20px")

            '''
            
            Timer (60) secs
            '''

            self.remaining_time = 60 # Countdown time in seconds

            self.tim = QLabel(str(self.remaining_time), self) #timer label
            self.tim.setGeometry(0, 0, 240, 150)
            self.tim.setStyleSheet(
                  "font-family: 'Times New Roman', Times, serif;"
                  "font-size: 20px")
            self.tim.move(10,10)
            
            

            
            self.timer = QTimer(self)
            self.timer.setInterval(1000)  # Update timer every second
            self.timer.timeout.connect(self.update_timer)
            self.timer.start()


            """
            Missing Words Label for showing the missing words
            """
            self.missing_words = QLabel('Missing:', self)
            self.missing_words.setFont(QFont('Times',10))
            self.missing_words.setGeometry(0, 0, 440, 220)
            self.missing_words.move(380,130)

    
            '''
            
            Random Sentence Label for showing the random sentence
            '''

            self.label = QLabel(sentence,self) #random Sentence Label
            self.setGeometry(0, 0, 900, 900)
            self.label.setGeometry(44, 40, 240, 120)
            
            self.label.setStyleSheet(
                  "font-family:  fantasy;"
                  "font-size: 13px")
            
            self.label.move(360,10)
            logging.debug(self.label.text())


            

            '''
            
            Accuracy label for showing the accuracy 
            '''
            self.accuracy = QLabel('Accuracy',self) #Accuracy Label
            self.accuracy.setFont(normal_font)
            self.accuracy.setGeometry(0, 0, 240, 120)
            self.accuracy.move(490,60)
            

          
            

            '''
            UserInput for typing the text
            
            '''

            self.userinput = QLineEdit(self) #userinput
            self.userinput.setMaxLength(40)
            self.userinput.setPlaceholderText('Enter your text')
            self.userinput.setGeometry(0, 0, 210, 20)
            self.userinput.move(370,90)
            self.userinput.setStyleSheet("border: 1px solid black;")
            self.userinput.setStyleSheet('background-color: white;')
   



            self.userinput.returnPressed.connect(self.return_pressed) #signals and slots for the userinput
            self.userinput.selectionChanged.connect(self.selection_changed)

            
            '''
            
            Clear Button for clearing the text
            '''

            clear_button = QPushButton("Clear",self)
            clear_button.setCheckable(True)
            clear_button.clicked.connect(self.clear_button)
            clear_button.setStyleSheet(
                "background-color: black;"
                "color: white;"
                "font-family: Tahoma, sans-serif;"
                "font-size: 12px;"
                "border-radius: 10px;"
            )
            clear_button.setGeometry(0, 0, 110, 40)
            clear_button.move(370,130)
            
            

            '''
            
            Enter Button for users to click enter
            '''
            self.enter_button = QPushButton('Click me',self)
            self.enter_button.clicked.connect(self.return_pressed)

            
        
            self.enter_button.setStyleSheet(
                "background-color: #55c2da;"
                "color: white;"
                "font-family: Tahoma, sans-serif;"
                "font-size: 12px;"
                "border-radius: 10px;"
            )
            self.enter_button.setGeometry(0, 0, 110, 40)
            self.enter_button.move(609,80)
            
           

            '''
            
            Selected Text Label for showing the selected text

            '''

            self.selected = QLabel('',self)
            self.selected.setGeometry(0, 0, 240, 120)
            self.selected.move(0,40)
            self.selected.setStyleSheet(
                "font-family: Tahoma, sans-serif;"
                "font-size: 12px;"
            )
            
            

            """

            layout = QVBoxLayout()
            layout.addWidget(self.label)
            layout.addWidget(self.accuracy)
            layout.addWidget(self.userinput)
            layout.addWidget(self.wpm)
            

            container = QWidget()
            container.setLayout(layout)
        

            self.setCentralWidget(container)

            """

   
     
    
    def calculating_accuracy(self,sentence:str,list_of_missing_words: List[str]) -> None:

        """ 
        This method calculates the accuracy of the user's input text.
        """
        count: int = 0
        for i,c in enumerate(sentence):
                        try:


                                
                                
                                if self.userinput.displayText()[i] == sentence[i]: #checking if the userinput matches the sentence
                                        count += 1
                                elif self.userinput.displayText()[i] != sentence[i]: #checkinf if the userinput doesn't matches the sentence
                                        
                                                
                                                missing_words = sentence[i].replace(' ',' ')
                                                
                                                list_of_missing_words.append(missing_words)

                                                
                                                 
                                        

                                        
                        except:
                                logging.debug('No matches')
                                
                        accuracy = round(count/len(sentence)* 100) #variable for accuracy
                        

                        new_missing_words = ''.join(list_of_missing_words) #missing words
                        
                        self.missing_words.setText(f'The missing words:{new_missing_words}') #updating missing words
                        self.accuracy.setText(str(f'Accuracy: {accuracy}')) #display the accuracy

                        if accuracy > 98:
                                self.missing_words.setText(f'No Missing Words')
                                self.missing_words.setStyleSheet(
                                        "color: green;"
                                        "font-family: 'Times New Roman', serif;"
                                        "font-size: 20px"
                                )

                                
                                logging.debug(self.userinput.validator())
                        if accuracy < 98:
                               self.missing_words.setStyleSheet(
                                        "color: black;"
                                        "font-family: 'Times New Roman', serif;"
                                        "font-size: 20px"
                                )
  
                        
        logging.debug(f'The accuracy {accuracy}')

        
   
    def clear_for_the_click_me_button(self):

        """ 
        This method is triggered when the user clicks on the "click me" button while the user input is empty.
        
        """
        if not self.userinput.text().strip():
                self.enter_button.clicked.disconnect()  # Disconnect all connections for clicked() signal
                self.enter_button.clicked.connect(self.clear_button)
        else:
                self.enter_button.clicked.disconnect()  # Disconnect all connections for clicked() signal
                self.enter_button.clicked.connect(self.return_pressed)


   
   
    def calculate_wpm_level(self,wpm: int) -> None:
        """
        This method calculates the WPM level based on the speed of the user's input.

           
        """
        accuracy_threshold = [10,50,60,90]
        if wpm <= accuracy_threshold[0]:
                self.score_label.setText('Very Low')
                
        elif wpm <= accuracy_threshold[1]:
                self.score_label.setText('Average')

        elif wpm >= accuracy_threshold[2] and wpm  <= accuracy_threshold[-1]:
               self.score_label.setText('Very High')
        elif wpm >= accuracy_threshold[-1]:
                self.score_label.setText('Mind-Blowing')

            
    def return_pressed(self):
                """
               This method updates the displayed words per minute (WPM) and accuracy when the user presses the enter key or clicks on the "click me" button.
                """
                

                logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


                start_time = time.time()   

                

                
                logging.debug('Entered')
               
                typing_words = self.userinput.displayText()

                sentence = self.label.text()

                
                if typing_words  == sentence: #checking if the typing_word is equal to sentence if it's then this code will execute
                        logging.debug('Right')
                
                

                end_time = max(time.time() - start_time, 1)

                elapsed_time = max(end_time - start_time, 1)

                typing_words = len(typing_words.split())


                
                wpm = round(typing_words / (elapsed_time / 60)/5) #the wpm variable

                


                logging.debug(f'The wpm is {str(wpm)}') 

                self.wpm.setText(str(f'WPM:{wpm}'))


                list_of_missing_words = []
                
                
                self.calculating_accuracy(sentence,list_of_missing_words) #calling the function for the accuracy
                self.calculate_wpm_level(wpm)
                self.clear_for_the_click_me_button()
                

               

    def selection_changed(self):
        """
        This method enables text selection and displays the selected text.
        """
        selected_text = self.userinput.selectedText()


        self.selected.setText(f"Selected Text is {selected_text}")
        logging.debug(selected_text)

                
    
    def clear_button(self):

        """
       This function clears the text entered by the user in the LineEdit.
        """
        if not self.userinput.text().strip():
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Fill Box")
                dlg.setText("Please Fill The Input")
                button = dlg.exec()


        self.userinput.setText('') 
        self.wpm.setText('WPM:') 
        self.accuracy.setText('Accuracy:')
        self.missing_words.setText('Missing:')
        self.score_label.setText('Score:')
        
        if self.timer.isActive():
                self.timer.stop()
                self.remaining_time = 60  
                self.tim.setText(f'Time: {str(self.remaining_time)}')  
                self.timer.start()
        else:
                self.tim.setText('Timer is not active')


        # start() will always restart the timer, no matter if it was active
        # or not, and will use the previously set interval (set with 
        # setInterval() or the last start() call
        
        

        

    

    
    def update_timer(self):
        """
        Updating the timer or countdown 
        to show the updated time
        """
        self.remaining_time -= 1
        self.tim.setText(f'Time:  {str(self.remaining_time)}')
 
        if self.remaining_time <= 0: #if the time equal to 0 or less than 0 then this code will execute
            self.timer.stop()
            self.label.setText("Time's up!")


if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = SpeedTyper()
        window.show()
        app.exec()