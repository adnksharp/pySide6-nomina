import sys
from notifypy import Notify as noty
import pyperclip as xclip

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hours = 0
        self.payment = 0
        self.lock = [False, False]
        
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.noty = noty()
        self.noty.title = 'Nomina'
        
        self.hparams = [40.0, 15.0, 15.0] # base, double hours and bonus
        self.hedit = [
            self.ui.hBase,
            self.ui.hTwo,
            self.ui.hPlus
        ]
        self.hlabel = [
            self.ui.hl1,
            self.ui.hl2,
            self.ui.hl3
        ]

        self.mparams = [3.5, 150.0, 220.0] # insurance, workers uninon, more deductios
        self.isrparams = [
            [8000.0, 13500.0, 25000], # max salary
            [0, 10, 19, 23] # isr to pay
        ]
        
        self.siriu = [
            [self.ui.isrM1, self.ui.isrM2, self.ui.isrM3],
            [self.ui.isrP1, self.ui.isrP2, self.ui.isrP3, self.ui.isrP4]
        ]
            
        self.medit = [
            self.ui.isrM1,
            self.ui.isrM2,
            self.ui.isrM3,
            self.ui.isrP1,
            self.ui.isrP2,
            self.ui.isrP3,
            self.ui.isrP4,
            self.ui.imss,
            self.ui.uDeductions,
            self.ui.mDeductions
        ]
        
        
        self.ui.hours.textChanged.connect(self.newHours)
        self.ui.payment.textChanged.connect(self.newPays)
        self.ui.hEdit.clicked.connect(self.changeHours)
        self.ui.dEdit.clicked.connect(self.changeDeductions)
        self.ui.pushButton_2.clicked.connect(self.copyToClipboard)
        self.ui.pushButton_4.clicked.connect(self.saveAs)
        
        for n in range(len(self.hedit)):
            self.hedit[n].textChanged.connect(self.updateHparams)
            
        for m in range(len(self.medit)):
            self.medit[m].textChanged.connect(self.updateDparams)
        
    def getPayroll(self):
        # hours worked
        hours = []
        try:
            _h = float(self.ui.hours.text())
        except:
            _h = 0
        
        if _h < 0:
            return    
        
        for i in range(len(self.hparams) - 1):
            if _h >= self.hparams[i]:
                hours.append(self.hparams[i])
                _h -= self.hparams[i]
            else:
                hours.append(_h)
                _h= 0
                break
        if _h > 0:
            hours.append(_h)
        for _ in range(3 - len(hours)):
            hours.append(0.0)
                
        # subtotal
        money = [ (hours[i] * (i+1) * self.payment) for i in range(len(hours))]
        money = sum(money)
        if hours[2] > 0:
            money += sum(hours) * self.payment * self.hparams[2] / 100
            
        # deductions
        for i in range(len(self.isrparams[0])):
            if money <= self.isrparams[0][i]:
                isr = self.isrparams[1][i]
                break
            if i == (len(self.isrparams[0]) - 1):
                isr = self.isrparams[1][i + 1]
        isr *= money / 100
        hs = money * self.mparams[0] / 100
        wu = self.mparams[1]
        md = self.mparams[2]
        
        self.ui.hTotal.setText(str(round(sum(hours[:3],2))))
        self.ui.hExtra.setText(str(round((hours[1] + hours[2]),2)))
        self.ui.dISR.setText('$ ' + str(round(isr,2)))
        self.ui.dIMSS.setText('$ ' + str(round(hs,2)))
        self.ui.dMore.setText('$ ' + str(round((md + wu),2)))
        self.ui.sTotal.setText('$ ' + str(round(money,2)))
        self.ui.aDeductions.setText('$ ' + str(round((isr + hs + wu + md),2)))
        self.ui.final_2.setText('$ ' + str(round((money - (isr + hs + wu + md)),2)))
        
        self.pout = f"""Horas totales    : {str(round(sum(hours[:3],2)))}
Horas extra      : {str(round((hours[1] + hours[2]),2))}
ISR              : $ {str(round(isr,2))}
Seguro           : $ {str(round(hs,2))}
Otras deducciones: $ {str(round((md + wu),2))}
Subtotal         : $ {str(round(money,2))}
Deducciones      : $ {str(round((isr + hs + wu + md),2))}

Total            : $ {str(round((money - (isr + hs + wu + md)),2))}"""
            
    def updateHparams(self):
        for k in range(len(self.hparams)):
            try:
                self.hparams[k] = float(self.hedit[k].text())
            except:
                return
        
        self.hlabel[0].setText(f'Base (0 a {str(self.hparams[0])})')
        self.hlabel[1].setText(f'Dobles ({str(self.hparams[0] + 0.01)} a {str(self.hparams[0] + self.hparams[1])})')
        self.hlabel[2].setText(f'Triples (>{str(self.hparams[0] + self.hparams[1])})\n+{str(self.hparams[2])})% de bonus')
    
        self.getPayroll()
    
    def updateDparams(self):
        for i in range(len(self.isrparams)):
            for j in range(len(self.isrparams[i])):
                try:
                    self. isrparams[i][j] = float(self.siriu[i][j].text())
                except:
                    pass
                
        for i in range(len(self.medit) - 7):
            try:
                self.mparams[i] = float(self.medit[7 + i].text())
            except:
                pass
        
        self.getPayroll()
    
    def newHours(self):
        try:
            self.hours = float(self.ui.hours.text())
        except:
            return
        self.getPayroll()
        
    def newPays(self):
        try:
            self.payment = float(self.ui.payment.text())
        except:
            return
        self.getPayroll()
        
    def changeHours(self):
        self.lock[0] = not self.lock[0]
        for i in self.hedit:
            i.setEnabled(self.lock[0])
            i.setStyleSheet('color:#fff;' if self.lock[0] else 'color:#888;')
        
    def changeDeductions(self):
        self.lock[1] = not self.lock[1]
        for i in self.medit:
            i.setEnabled(self.lock[1])
            i.setStyleSheet('color:#fff;' if self.lock[1] else 'color:#888;')
        
    def copyToClipboard(self):
        try:
            xclip.copy(self.pout)
            self.noty.message = 'Datos copiados al portapapeles'
            self.noty.send()
        except: 
            pass
        
    def saveAs(self):
        try:
            fileName, _ =  QFileDialog.getSaveFileName(self, 
                "Guardar datos de nomina", "", "Text Files(*.txt)")
            if fileName:
                if not '.txt' in fileName:
                    fileName += '.txt'
                with open(fileName, 'w') as f:
                    f.write(self.pout)
            self.noty.message = f'Archivo {fileName.split("/")[-1]} guardado'
        except:
            self.noty.message = 'No se pugo guardar el archivo'
        self.noty.send()
            #self.fileName = fileName
            #self.setWindowTitle(str(os.path.basename(fileName)) + " - Notepad Alpha[*]")
        #QFiledialog or exec

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
