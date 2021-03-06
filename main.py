#command "pip install -r requirements.txt" voor het installeren van de nodige dependencies
# pip install -r requirements.txt

import cherrypy
import psutil

class Monitoring(object):
    @cherrypy.expose
    def index(self):

        #RAM GEDEELTE
        checkRam1 = psutil.virtual_memory()[0] / 1073741274
        #Bovenstaande deelsom wordt gemaakt om de gegeven MB te converten in GB

        showTotalRam = "Totaal werkgeheugen gedetecteerd: ", checkRam1, "GB"

        checkRam2 = psutil.virtual_memory()[1] / 1073741274, 'GB'
        checkRamFree = psutil.virtual_memory()[4] / 1073741274
        checkFreeRamPer = (checkRamFree / checkRam1) * 100

        showFreeRam = "Hiervan is: ", checkRamFree, "GB vrij, dat is", checkFreeRamPer, "%"

        checkRamPer = 'Er is dus: ', psutil.virtual_memory()[2], 'aan RAM percentage in gebruik'
        show_Ram = str(showTotalRam) + str(showFreeRam) + str(checkRamPer)



        #CPU GEDEELTE
        CoreCount = psutil.cpu_count(logical=False)
        ThreadCount = psutil.cpu_count()
        checkCPU = 'CPU met', CoreCount, 'Cores en', ThreadCount, 'Threads met de orginele', \
                   psutil.cpu_freq()[0] / 1000, 'GHz'
        show_CPU = str(checkCPU)


        #DISK GEDEELTE
        checkDisk1 = 'Schijfopslag in gebruik van waar op dit moment de software op wordt uitgevoerd: ', \
                    psutil.disk_usage('/')[1] / 1073741274, 'GB'
        # Bovenstaande deelsom wordt opnieuw gemaakt om de gegeven MB te converten in GB

        checkDisk2 = 'Schijfopslag vrij van waar op dit moment de software op wordt uitgevoerd: ', \
                    psutil.disk_usage('/')[2] / 1073741274, 'GB'
        checkDisk3 = 'Schijfopslag vrij in % van waar op dit moment de software op wordt uitgevoerd: ', \
                    psutil.disk_usage('/')[3]

        TotalcheckDisk = checkDisk1 + checkDisk2 + checkDisk3

        show_Disk = str(TotalcheckDisk)


        #RETURN GEDEELTE (Wat weergegeven wordt op de HTML Pagina)
        return show_Ram + show_CPU + show_Disk + show_CPU

cherrypy.quickstart(Monitoring())
