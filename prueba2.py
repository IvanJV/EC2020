import re

def RisToCSV(ris_file):
    
    URs = re.findall(r'(?<=UR  - )(.*)', ris_file)
    TIs = re.findall(r'(?<=TI  - )(.*)', ris_file)
    ABs = re.findall(r'(?<=AB  - )(.*)', ris_file)

    ris = ''
    for ur,ti,ab in zip(URs,TIs,ABs):
        ris += ur + '\t' + ti + '\t' + ab + '\n'

    return ris

ris_file = """TY  - JOUR
TI  - Chronic cough due to acute bronchitis: ACCP evidence-based clinical practice guidelines.
PY  - 2006
AU  - Braman SS
AU  - Braman, Sidney S
AB  - BACKGROUND: The purpose of this review is to present the evidence for the diagnosis and treatment of cough due to acute bronchitis and make recommendations that will be useful for clinical practice. Acute bronchitis is one of the most common diagnoses made by primary care clinicians and emergency department physicians. It is an acute respiratory infection with a normal chest radiograph that is manifested by cough with or without phlegm production that lasts for up to 3 weeks. Respiratory viruses appear to be the most common cause of acute bronchitis; however, the organism responsible is rarely identified in clinical practice because viral cultures and serologic assays are not routinely performed. Fewer than 10% of patients will have a bacterial infection diagnosed as the cause of bronchitis. The diagnosis of acute bronchitis should be made only when there is no clinical or radiographic evidence of pneumonia, and the common cold, acute asthma, or an exacerbation of COPD have been ruled out as the cause of cough. Acute bronchitis is a self-limited respiratory disorder, and when the cough persists for >3 weeks, other diagnoses must be considered.METHODS: Recommendations for this review were obtained from data using a National Library of Medicine (PubMed) search dating back to 1950, which was performed in August 2004. The search was limited to literature published in the English language and human studies, using search terms such as "cough," "acute bronchitis," and "acute viral respiratory infection."RESULTS: Unfortunately, most previous controlled trials guiding the treatment of acute bronchitis have not vigorously differentiated acute bronchitis and the common cold, and also have not distinguished between an acute exacerbation of chronic bronchitis and acute asthma as a cause of acute cough. For patients with the putative diagnosis of acute bronchitis, routine treatment with antibiotics is not justified and should not be offered. Antitussive agents are occasionally useful and can be offered as therapy for short-term symptomatic relief of coughing, but there is no role for inhaled bronchodilator or expectorant therapy. Children and adult patients with confirmed and probable whooping cough should receive a macrolide antibiotic and should be isolated for 5 days from the start of treatment; early treatment within the first few weeks will diminish the coughing paroxysms and prevent spread of the disease; the patient is unlikely to respond to treatment beyond this period.CONCLUSION: Acute bronchitis is an acute respiratory infection that is manifested by cough and, at times, sputum production that lasts for no more than 3 weeks. This syndrome should be distinguished from the common cold, an acute exacerbation of chronic bronchitis, and acute asthma as the cause of acute cough. The widespread use of antibiotics for the treatment of acute bronchitis is not justified, and vigorous efforts to curtail their use should be encouraged.
UR  - http://www.epistemonikos.org/documents/0f8b5c48838a36541497f4d318c92297c3fa68e3
T2  - CHEST
VL  - 129
SP  - 95-95
IS  - 1 Suppl
SN  - 00123692
DO  - 10.1378/chest.129.1_suppl.95S
U1  - 16428698[pmid]
ER  - 


TY  - JOUR
TI  - Antibiotics for the common cold and acute purulent rhinitis.
PY  - 2013
AU  - Kenealy T
AU  - Arroll B
AB  - BACKGROUND: It has long been believed that antibiotics have no role in the treatment of common colds yet they are often prescribed in the belief that they may prevent secondary bacterial infections. OBJECTIVES: To determine the efficacy of antibiotics compared with placebo for reducing general and specific nasopharyngeal symptoms of acute upper respiratory tract infections (URTIs) (common colds).To determine if antibiotics have any influence on the outcomes for acute purulent rhinitis and acute clear rhinitis lasting less than 10 days before the intervention.To determine whether there are significant adverse outcomes associated with antibiotic therapy for participants with a clinical diagnosis of acute URTI or acute purulent rhinitis. SEARCH METHODS: For this 2013 update we searched CENTRAL 2013, Issue 1, MEDLINE (March 2005 to February week 2, 2013), EMBASE (January 2010 to February 2013), CINAHL (2005 to February 2013), LILACS (2005 to February 2013) and Biosis Previews (2005 to February 2013). SELECTION CRITERIA: Randomised controlled trials (RCTs) comparing any antibiotic therapy against placebo in people with symptoms of acute upper respiratory tract infection for less than seven days, or acute purulent rhinitis less than 10 days in duration. DATA COLLECTION AND ANALYSIS: Both review authors independently assessed trial quality and extracted data. MAIN RESULTS: This updated review included 11 studies. Six studies contributed to one or more analyses related to the common cold, with up to 1047 participants. Five studies contributed to one or more analyses relating to purulent rhinitis, with up to 791 participants. One study contributed only to data on adverse events and one met the inclusion criteria but reported only summary statistics without providing any numerical data that could be included in the meta-analyses. Interpretation of the combined data is limited because some studies included only children, or only adults, or only males; a wide range of antibiotics were used and outcomes were measured in different ways. There was a moderate risk of bias because of unreported methods details or because an unknown number of participants were likely to have chest or sinus infections.Participants receiving antibiotics for the common cold did no better in terms of lack of cure or persistence of symptoms than those on placebo (risk ratio (RR) 0.95, 95% confidence interval (CI) 0.59 to 1.51, (random-effects)), based on a pooled analysis of six trials with a total of 1047 participants. The RR of adverse effects in the antibiotic group was 1.8, 95% CI 1.01 to 3.21, (random-effects). Adult participants had a significantly greater risk of adverse effects with antibiotics than with placebo (RR 2.62, 95% CI 1.32 to 5.18) (random-effects) while there was no greater risk in children (RR 0.91, 95% CI 0.51 to 1.63).The pooled RR for persisting acute purulent rhinitis with antibiotics compared to placebo was 0.73 (95% CI 0.47 to 1.13) (random-effects), based on four studies with 723 participants. There was an increase in adverse effects in the studies of antibiotics for acute purulent rhinitis (RR 1.46, 95% CI 1.10 to 1.94). AUTHORS' CONCLUSIONS: There is no evidence of benefit from antibiotics for the common cold or for persisting acute purulent rhinitis in children or adults. There is evidence that antibiotics cause significant adverse effects in adults when given for the common cold and in all ages when given for acute purulent rhinitis. Routine use of antibiotics for these conditions is not recommended.
UR  - http://www.epistemonikos.org/documents/177eb71442d2ef8dcf2811559a3ff13314275b5e
T2  - Cochrane database of systematic reviews (Online)
VL  - 6
SP  - CD000247
IS  - 6
SN  - 1469-493X
DO  - 10.1002/14651858.CD000247.pub3
U1  - 23733381[pmid]
ER  - """

print(RisToCSV(ris_file))