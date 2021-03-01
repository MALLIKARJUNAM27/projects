#
#   Data verification Report Generation
#

import xml.etree.ElementTree as ET      # for XML parsing
#import XML_functions as xf      # for XML parsing
import csv
import os   # for os.linesep

import time
time_begin=time.time()
time_b = int(time_begin)
time_b_str = str(time_b)
print("\n================================ BEGIN_REPORT_BUILD ================================")
print("Begin Time : {}".format(time.strftime("%A %d %B %Y %H:%M:%S")))

# Fichier input
sep = "\t" #separator
############################################################################################
#
#	XML FILES
#
############################################################################################
#	INFRA
############################################################################################
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/Infrastructure/NH- Workspace/VEVPF_3.10.4.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.15.2/1-SystemDatabase/Infrastructure/VEVPF.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_4.3.2.1/1-SystemDatabase/Infrastructure/VEVPF.xml"
# verifFile1 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/1-SystemDatabase_3.12.18.1/1-SystemDatabase/Infrastructure/_VEVPF.xml"
#verifFile1 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/BL 1.3.1- MDL 4.x.x/PA_CTRL_Data_4.5.1.1/1-SystemDatabase/Infrastructure/VEVPF.xml"

# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/Infrastructure/NH- Workspace/VE/VE.3.10.5.7420.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_4.3.2.1/1-SystemDatabase/Infrastructure/VE.xml"

#LIGNEGAT
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_4.3.2.1/1-SystemDatabase/Infrastructure/LigneGAT.xml"
# verifFile2 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/1-SystemDatabase_3.12.18.1_Draft4/1-SystemDatabase/Infrastructure/LigneGAT.xml"
# verifFile2 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/BL 1.3.1- MDL 4.x.x/PA_CTRL_Data_4.5.1.1/1-SystemDatabase/Infrastructure/LigneGAT.xml"
#verifFile2 = "C:/U500/CDS verification/1.3.3.6_BETA3/lillel1_control_parameters-2.4.2/lillel1_control_parameters-2.4.2/Compilation/CDS_parameters.xml"
#verifFile2 =input("Please enter the input xml file with path")
verifFile2 = r"SZL20_TT.xml"

#VE4C
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/3.12.15/1-SystemDatabase/Infrastructure/VE.3.12.15.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.12.2/1-SystemDatabase/Infrastructure/VE.xml"
#verifFile3 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/BL 1.3.1- MDL 4.x.x/PA_CTRL_Data_4.5.1.1/1-SystemDatabase/Infrastructure/VE.xml"

############################################################################################
#	RS
############################################################################################
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Formation_Characteristics_Val208.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Formation_Characteristics_NMR.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/NH- Workspace/Train_Unit_Characteristics_Val208_3.10.2.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/NH- Workspace/Train_Unit_Characteristics_NMR_3.10.2.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/NH- Workspace/Lille_Train_Unit_Infra_Val208.main_PA_CTRL_int_2_3.10.6.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/NH- Workspace/Lille_Train_Unit_Infra_NMR.main_PA_CTRL_int_2_3.10.6.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Formation_Characteristics_NMR.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Formation_Characteristics_VAL208.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Unit_Characteristics_Val208.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Unit_Characteristics_NMR.xml"
############################################################################################
#	SETTINGS
############################################################################################
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/U500Settings/NH- Workspace/U500Settings_commun_withpublishedData_3.10.1.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/U500Settings/U500Settings_commun_withpublishedData_3.6.1.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.12.2/1-SystemDatabase/U500Settings/U500Settings_commun.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_4.3.2.1/1-SystemDatabase/U500Settings/U500Settings_commun.xml"
#verifFile4 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/BL 1.3.1- MDL 4.x.x/PA_CTRL_Data_4.5.1.1/1-SystemDatabase/U500Settings/U500Settings_commun.xml"

# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.5.4/PA_CTRL_Data/1-SystemDatabase/U500Settings/U500Settings_VEVPF.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/U500Settings/NH- Workspace/U500Settings_VE_withpublishedData.main_PA_CTRL_int_PA_CTRL_INT_3.10_4_3.10.6.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/U500Settings/U500Settings_VE.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.4.3/PA_CTRL_Data/1-SystemDatabase/U500Settings/U500Settings_LigneGAT.xml"


############################################################################################
#	SERVICES
############################################################################################
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/Services/NH- Workspace/VEVPF_Services.3.10.1.xml"
# verifFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/Services/NH- Workspace/VE_Services.main_PA_CTRL_int_12_3.10.6.xml"
# verifFile4 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/1-SystemDatabase_3.12.18.1_Draft4/1-SystemDatabase/Services/LigneGAT_Services.xml"

############################################################################################
#
#	REPORT FILES
#
############################################################################################
#	INFRA
############################################################################################
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/Infrastructure/NH- Workspace/VEVPF_3.10.4.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.15.2/1-SystemDatabase/Infrastructure/VEVPF_3.12.15.2.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/Infrastructure/NH- Workspace/VE/VE.3.10.5.7420.csv"
#reportFile1 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/BL 1.3.1- MDL 4.x.x/PA_CTRL_Data_4.5.1.1/1-SystemDatabase/Infrastructure/VEVPF_4.5.1.1.csv"
# reportFile1 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/1-SystemDatabase_3.12.18.1_Draft4/1-SystemDatabase/Infrastructure/VEVPF_3.12.18_DRAFT.csv"

# REPORT LIGNEGAT
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_4.3.2.1/1-SystemDatabase/Infrastructure/LigneGAT_4.3.2.1_SeparatedAttributes.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.13.4/PA_CTRL_Data_3.12.13.4/1-SystemDatabase/Infrastructure/LigneGAT_3.12.13.4.csv"
# reportFile2 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/1-SystemDatabase_3.12.18.1_Draft4/1-SystemDatabase/Infrastructure/LigneGAT_3.12.18_DRAFT.csv"
# reportFile2 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/BL 1.3.1- MDL 4.x.x/PA_CTRL_Data_4.5.1.1/1-SystemDatabase/Infrastructure/LigneGAT_4.5.1.1.csv"
#reportFile2 = "C:/U500/CDS verification/1.3.3.6_BETA3/lillel1_control_parameters-2.4.2/lillel1_control_parameters-2.4.2/Compilation/CDS_parameters.csv"
#reportFile2 = input("Please enter output file name ( output.csv) with path")
reportFile2 = "SZL20_TT.csv"
# REPORT VE4C
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.12.2/1-SystemDatabase/Infrastructure/VE4C.3.12.12.2.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/3.12.15/1-SystemDatabase/Infrastructure/VE4C.3.12.15.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_4.3.2.1/1-SystemDatabase/Infrastructure/VE4C_4.3.2.1.csv"
# reportFile3 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/BL 1.2.2 - MDL 3.x.x/PA_CTRL_Data_3.12.18.1/1-SystemDatabase/Infrastructure/VE4C_3.12.18_test_id_name.csv"
# reportFile3 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/BL 1.3.1- MDL 4.x.x/PA_CTRL_Data_4.5.1.1/1-SystemDatabase/Infrastructure/VE4C_4.5.1.1.csv"

############################################################################################
#	RS
############################################################################################
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Formation_Characteristics_Val208.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Formation_Characteristics_NMR.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/NH- Workspace/Train_Unit_Characteristics_Val208_3.10.2.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/RollingStock/NH- Workspace/Train_Unit_Characteristics_NMR_3.10.2.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/1- Rapport de Verif/1- Rapport de verif data/3.10.5/VE4C/Lille_Train_Unit_Infra_Val208.3.10.6.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/1- Rapport de Verif/1- Rapport de verif data/3.10.5/VE4C/Lille_Train_Unit_Infra_NMR.3.10.6.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Formation_Characteristics_NMR.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Formation_Characteristics_VAL208_3.12.2.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Unit_Characteristics_Val208_3.12.2.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/RollingStock/Train_Unit_Characteristics_NMR_3.12.2.csv"
############################################################################################
#	SETTINGS
############################################################################################
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/U500Settings/NH- Workspace/U500Settings_commun_withpublishedData_3.10.1.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/U500Settings/U500Settings_commun_withpublishedData_3.6.1.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.12.2/1-SystemDatabase/U500Settings/U500Settings_commun_3.12.12.2.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.5.4/PA_CTRL_Data/1-SystemDatabase/U500Settings/U500Settings_VEVPF.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_4.3.2.1/1-SystemDatabase/U500Settings/U500Settings_commun_SeparateAttributes_v2.csv"
# reportFile4 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/BL 1.3.1- MDL 4.x.x/PA_CTRL_Data_4.5.1.1/1-SystemDatabase/U500Settings/U500Settings_commun_4.5.1.1.csv"

# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/U500Settings/NH- Workspace/U500Settings_VE4C_withpublishedData_3_10_6.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/1- Rapport de Verif/1- Rapport de verif data/3.10.5/VE4C/U500Settings_VE4C_withpublishedData_3_10_6.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.2/PA_CTRL_Data/1-SystemDatabase/U500Settings/U500Settings_VE_3.12.2.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/PA_CTRL_Data_3.12.4.3/PA_CTRL_Data/1-SystemDatabase/U500Settings/U500Settings_LigneGAT_3.12.4.csv"

############################################################################################
#	SERVICES
############################################################################################
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/Services/NH- Workspace/VEVPF_Services.3.10.1.csv"
# reportFile = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/100726348_CC_VIEW/100726348_PA_CTRL_int/projets/lille_ccst/PA_CTRL_Data/1-SystemDatabase/Services/NH- Workspace/VE4C_Services.3.10.6.csv"
# reportFile4 = "D:/Documents and Settings/100726348/2- U500/00-Livraison Datas/3- Data saved/1-SystemDatabase_3.12.18.1_Draft4/1-SystemDatabase/Services/LigneGAT_Services.3.12.18_DRAFT.csv"

# verifEntete = "Element"+sep+"Path"+sep+"Parameters"+sep+"Verified"+sep+"Verified by"+sep+\
              # "Input"+sep+"Conform to Input"+sep+"Conform to Input Rationale"+sep+ \
              # "Conform to PrPD"+sep+"Conform to PrPD rationale"+sep+"Conform to SyPD"+sep+\
              # "Conform to SyPD rationale"+sep+"Global Result"+sep+"Last verified database version\n"
verifEntete = ["Element", "Path", "Parameters", "Main ID element", "Main NAME element"]


# fucntion compute elt generate report corresponding to the element in parameter
# def computeElt(element, level, path, file):
def computeElt(element, level, path, report, Name_saved, id_saved):
	line = ['', '', '', '', '', '', '', '', '' ,'' ,'' ,'', '', '', '', ''] # Déclaration de lignes vide pour le csv

	#######################################################################################################################################
	# 1- AFFICHER LES ATTRIBUTS XML DANS UNE SEULE CELLULE "EXCEL"	
	#######################################################################################################################################
    # #parameters list
	# params='"' # Définir les attributs entre les guillemets. Ici guillemet du début
	# for param in element.attrib.items(): # Pour tous les attributs de l'élément
		# params += '{}={}\n'.format(param[0], param[1])  # ici en exemple on aura dans le csv : PSRSpeed value = 10
	# params += '"' # ici fin des guillemets

	# line[0:3] = [element.tag, path, params] # 
		
	#######################################################################################################################################
	# 2- SEPARER TOUS LES ATTRIBUTS XML DANS DIFFENTES CELLULES "EXCEL"	
	#######################################################################################################################################	
	
	for param in element.attrib.items(): # Pour tous les attributs de l'élément
		
		##############################################################################################################	
		# §NKH§ Amélioration de l'outil : identifier pour toutes les données l'id et le name de l'attribut
		##############################################################################################################		
			
		if param[0]=='name' : # §NKH§ # détecter le paramètre 'name' et prendre sa valeur
			Name='NAME={}\n'.format(param[1]) # §NKH§ 

		if param[0]=='id' : # §NKH§ # détecter le paramètre 'name' et prendre sa valeur
			id='ID={}\n'.format(param[1]) # §NKH§ 
			
		params = '{}={}\n'.format(param[0], param[1]) # §NKH§   # ici en exemple on aura dans le csv : PSRSpeed value = 10
		# line[0:3] = [element.tag, path, params]
		# line[0:5] = [element.tag, path, params, id, Name] # §NKH§ 
		try:
			Name
		except NameError:
			line[0:5] = [element.tag, path, params, id_saved, Name_saved] # §NKH§ 
		else:
			try:
				id
			except NameError:
				line[0:5] = [element.tag, path, params, id_saved, Name] # §NKH§
			else:	
				line[0:5] = [element.tag, path, params, id, Name] # §NKH§ 
				Name_saved = Name
				id_saved = id
		report.writerow(line) # afficher dans le csv
		
	for subElement in element:
		computeElt(subElement, level+1, path + subElement.tag+'/', report, Name_saved,id_saved)
		
def reportGen():
    
	Name_saved = None
	id_saved = None
    # Open & parse file
	#verifFiles_ReportFiles = [[verifFile1,reportFile1],
	#						  [verifFile2,reportFile2],
	#						  [verifFile3,reportFile3],
	#						  [verifFile4,reportFile4]]
	verifFiles_ReportFiles = [[verifFile2,reportFile2]]
	for Matrix in verifFiles_ReportFiles: 	
		# print(Matrix[0])	
		try:
			with open(Matrix[0]) :pass 
			verifTree = ET.parse(Matrix[0])
			# Get xml tree structure
			verifRoot = verifTree.getroot()
			with open(Matrix[1], 'w') as csvfile :
				reportwriter = csv.writer(csvfile, delimiter=';', lineterminator='\n') #, quotechar='|', quoting=csv.QUOTE_MINIMAL)                            
				reportwriter.writerow(verifEntete)        
			# Browse tree
				computeElt(verifRoot, 0, '/', reportwriter,Name_saved,id_saved)
		except IOError:
			print("\n\nMissing Input File : {}. The verification is not done for this file... Continue Data verification anyway".format(Matrix[0]))

reportGen()

	
time_end=time.time()
executed_time=time_end-time_begin
executed_time=round(executed_time,2)
def convSec(executed_time):
	q,s=divmod(executed_time,60)
	h,m=divmod(q,60)
	return "%dh %dmin %ds" %(h,m,s)
convSec(executed_time)
print("\n-------------------EXECUTED TIME --------------------------")
print("\nEnd Time : {}".format(time.strftime("%A %d %B %Y %H:%M:%S")))
print("Executed time : {} secondes. Soit : {}".format(executed_time,convSec(executed_time)))
print("\n================================ REPORT_BUILD_END ================================")