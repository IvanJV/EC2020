# Prueba Epistemonikos

A continuación se presenta una serie de 3 pruebas para testear habilidades de programación de los postulantes.
Las pruebas pueden ser desarrolladas tanto en Python como en Javascript
Todo lo que recibamos será utilizado únicamente para medir las habilidades de los postulantes. No utilizaremos el código para ningún otro propósito.

## 1.- Web scraping

Desarrollar una función que sea capaz de obtener un listado con todos los nombres de productos de una búsqueda en el sitio https://salcobrand.cl.
La función debe recibir un string con la búsqueda a realizar en la página y debe retornar un listado con los nombres de los productos que aparecen en el sitio

### Ejemplo 1:

```
    Input: "Aspirina"
    Output: [
        "Aspirina adulto 500mg caja de 10 tiras",
        "Aspirina forte 650mg caja de 8 tiras",
        "Aspirina pediátrica de 100mg caja de 7 tiras",
        "Acido Acetilsalicilico 500Mg Oral Solido",
        "Acido Acetilsalicilico 500Mg Oral Solido",
        "Acido Acetilsalicilico 100Mg Oral Solido",
        "Acido Acetilsalicilico 650Mg Oral Solido",
        "Acido Acetilsalicilico 100Mg Oral Solido"
    ]
```

### Ejemplo 2:

```
    Input: "Pasta de dientes"
    Output: [
        "Pasta Dental Anticaries Neutrazúcar ",
        "Pasta Dental Professional Natural Protection Encías ",
        "Pasta de dientes infantil MINIONS",
        "Pasta de dientes Total 12 Aliento Salud",
        "Pasta de Dientes Sensitive",
        "Pasta Dental Total",
        "Pasta Dental Repara y Protege Variedades",
        "Pasta de Dientes White Now ",
        "Pasta de Dientes White Now ",
        "Pasta Dental Professional Natural Protection Esmalte y Encías",
        "Pasta de Dientes White Now",
        "Pasta de Dientes Integral 18 hrs. Resist +",
        "Pasta de Dientes White Now Glossy Chic ",
        "Pasta de dientes Max White 3x2",
        "Pasta Dental Luminous White ",
        "Pasta Dental Repara y Protege Variedades",
        "Pasta Dental Repara y Protege Variedades",
        "Pasta Dental para la Prevención de Caries ",
        "Pasta Dental Max White Crystal Mint ",
        "Pasta de dientes PAW PATROL",
        "Pasta Dental Sensitive ",
        "Pasta Dental White Now para Hombre Super Pure",
        "Pasta de dientes SOY LUNA",
        "Pasta de diente infantil Barbie",
        "Pasta Dental 3D White Sensitive Care",
        "Pasta Dental Professional Natural Protection Sensitive",
        "Pasta Dental Sensitive Proalivio ",
        "Pack Pasta Dental Pepsodent Triple Más  ",
        "Pack pasta dental Xtra Whitening ",
        "Pasta Dental para Dientes Sensibles",
        "Pasta Dental Niños Jun Barney ",
        "Pasta Dental Minipep 2 a 6 años ",
        "Tripack de pasta de dientes Total 12 ",
        "Pasta dental sabor menta",
        "Pasta Dental 3D White  ",
        "Pack pasta dientes Triple Acción ",
        "Pasta Dental Star Wars",
        "Pasta dentrífica White, blanqueadora",
        "Pasta Dental Stage Frozen Sabor a Frutas",
        "Pasta Dental Infantil Sabor Frutas Silvestres",
        "Pack Pasta Pepsodent Bi- Active ",
        "Pack Pasta Dental White Now ",
        "Pasta Dental Complete Protection",
        "Pack de Cepillo y Mini Pasta Dental Dientes Sensibles"
    ]
```
## 2.- Procesamiento de un archivo

Desarrollar una función que sea capaz de leer un string en formato RIS <https://en.wikipedia.org/wiki/RIS_(file_format)> (viene un archivo de ejemplo incluido) y convertirlo en un string en formato TSV <https://en.wikipedia.org/wiki/Tab-separated_values> donde cada fila corresponda a un paper y las columnas deben contener la siguiente información: 
- Columna 1: URL de epistemonikos (campo UR del archivo RIS)
- Columna 2: Título de la referencia (campo TI del archivo RIS)
- Columna 3: Abstract de la referencia (campo AB del archivo RIS)

OJO, no es necesario que la función lea el archivo. La función tiene que recibir un string en formato RIS y devolver otro string, pero en formato TSV

### Ejemplo 1

```
    Input:
"""TY  - JOUR
TI  - Do delayed prescriptions reduce antibiotic use in respiratory tract infections? A systematic review.
PY  - 2003
AU  - Arroll B
AU  - Kenealy T
AU  - Kerse N
AB  - BACKGROUND: There is concern about the increasing resistance of antibiotics to common bacteria. Delayed prescribing for respiratory tract infections is a strategy that may reduce the use of antibiotics. AIM: To systematically review controlled trials of delayed prescriptions to establish their capacity to reduce antibiotic intake. DESIGN OF STUDY: A systematic review of the literature. SETTING: Four studies were conducted in the United Kingdom and one in New Zealand. METHODS: We searched MEDLINE from 1966 to April 2003, EMBASE, and the Cochrane Controlled Trials Register using the following terms: 'delayed', 'antibiotics', 'prescriptions', and 'back-up' (as in back-up prescription). We included controlled trials of studies in which the intervention was a delayed prescription compared to an immediate prescription for patients with upper respiratory tract infections. The studies were selected independently and the results compared. Disagreements were resolved by discussion. The data and quality of the studies were extracted and assessed independently by two of the authors. RESULTS: Four randomised controlled trials and one before-after controlled trial contributed to the review. The relative risk in the randomised trials for lower antibiotic usage when a delayed prescription was given ranged from 0.54 for the common cold to 0.25 for otitis media. CONCLUSION: The consistent reduction in antibiotic usage in the five controlled trials included in this review suggests that delayed prescription is an effective means of reducing antibiotic usage for acute respiratory infections. The duration of delay for prescriptions ranged widely, from 1 to 7 days.
UR  - http://www.epistemonikos.org/documents/0881d4dd5dedec801eb46c417c1c8037b7ee81cd
T2  - The British journal of general practice : the journal of the Royal College of General Practitioners
VL  - 53
SP  - 871-7
IS  - 496
SN  - 0960-1643
U1  - 14702908[pmid]
ER  - 


TY  - JOUR
TI  - A systematic review of the risks factors associated with the onset and natural progression of hydrocephalus.
PY  - 2017
AU  - Walsh S
AU  - Donnan J
AU  - Morrissey A
AU  - Sikora L
AU  - Bowen S
AU  - Collins K
AU  - MacDonald D
AB  - The purpose of this study was to systematically assess and synthesize the world literature on risk factors for the onset and natural progression of hydrocephalus, thereby providing a basis for policy makers to identify appropriate risk management measures to mitigate the burden of disease in Canada. Evidence for risk factors was limited for both onset and progression. Two meta-analyses that examined a risk factor for onset met the inclusion criteria. One found a significant protective effect of prenatal vitamins among case control studies, but not cohort/randomized controlled trials (RCTs). The second found maternal obesity to be a significant risk factor for congenital hydrocephalus. Significant risk factors among 25 observational studies included: biological (multiple births, maternal parity, common cold with fever, maternal thyroid disease, family history, preterm birth, hypertension, ischemic heart disease, ischemic ECG changes, higher cerebrospinal fluid protein concentration following vestibular schwannoma); lifestyle (maternal obesity, high-density lipoprotein (HDL) cholesterol, maternal diabetes, maternal age), healthcare-related (caesarean section, interhospital transfer, drainage duration following subarachnoid hemorrhage, proximity to midline for craniectomy following traumatic brain injury); pharmaceutical (prenatal exposure to: tribenoside, metronidazole, anesthesia, opioids); and environmental (altitude, paternal occupation). Three studies reported on genetic risk factors: no significant associations were found. There are major gaps in the literature with respect to risk factors for the natural progression of hydrocephalus. Only two observational studies were included and three factors reported. Many risk factors for the onset of hydrocephalus have been studied; for most, evidence remains limited or inconclusive. More work is needed to confirm any causal associations and better inform policy.
UR  - http://www.epistemonikos.org/documents/0eec83d79a0db0ab06068ff240125554e01c1f37
T2  - Neurotoxicology
VL  - 61
SP  - 33-45
SN  - 1872-9711
DO  - 10.1016/j.neuro.2016.03.012
U1  - 27000516[pmid]
ER  - """

    Output: 
"""http://www.epistemonikos.org/documents/0881d4dd5dedec801eb46c417c1c8037b7ee81cd	Do delayed prescriptions reduce antibiotic use in respiratory tract infections? A systematic review.	BACKGROUND: There is concern about the increasing resistance of antibiotics to common bacteria. Delayed prescribing for respiratory tract infections is a strategy that may reduce the use of antibiotics. AIM: To systematically review controlled trials of delayed prescriptions to establish their capacity to reduce antibiotic intake. DESIGN OF STUDY: A systematic review of the literature. SETTING: Four studies were conducted in the United Kingdom and one in New Zealand. METHODS: We searched MEDLINE from 1966 to April 2003, EMBASE, and the Cochrane Controlled Trials Register using the following terms: 'delayed', 'antibiotics', 'prescriptions', and 'back-up' (as in back-up prescription). We included controlled trials of studies in which the intervention was a delayed prescription compared to an immediate prescription for patients with upper respiratory tract infections. The studies were selected independently and the results compared. Disagreements were resolved by discussion. The data and quality of the studies were extracted and assessed independently by two of the authors. RESULTS: Four randomised controlled trials and one before-after controlled trial contributed to the review. The relative risk in the randomised trials for lower antibiotic usage when a delayed prescription was given ranged from 0.54 for the common cold to 0.25 for otitis media. CONCLUSION: The consistent reduction in antibiotic usage in the five controlled trials included in this review suggests that delayed prescription is an effective means of reducing antibiotic usage for acute respiratory infections. The duration of delay for prescriptions ranged widely, from 1 to 7 days.
http://www.epistemonikos.org/documents/0eec83d79a0db0ab06068ff240125554e01c1f37	A systematic review of the risks factors associated with the onset and natural progression of hydrocephalus.	The purpose of this study was to systematically assess and synthesize the world literature on risk factors for the onset and natural progression of hydrocephalus, thereby providing a basis for policy makers to identify appropriate risk management measures to mitigate the burden of disease in Canada. Evidence for risk factors was limited for both onset and progression. Two meta-analyses that examined a risk factor for onset met the inclusion criteria. One found a significant protective effect of prenatal vitamins among case control studies, but not cohort/randomized controlled trials (RCTs). The second found maternal obesity to be a significant risk factor for congenital hydrocephalus. Significant risk factors among 25 observational studies included: biological (multiple births, maternal parity, common cold with fever, maternal thyroid disease, family history, preterm birth, hypertension, ischemic heart disease, ischemic ECG changes, higher cerebrospinal fluid protein concentration following vestibular schwannoma); lifestyle (maternal obesity, high-density lipoprotein (HDL) cholesterol, maternal diabetes, maternal age), healthcare-related (caesarean section, interhospital transfer, drainage duration following subarachnoid hemorrhage, proximity to midline for craniectomy following traumatic brain injury); pharmaceutical (prenatal exposure to: tribenoside, metronidazole, anesthesia, opioids); and environmental (altitude, paternal occupation). Three studies reported on genetic risk factors: no significant associations were found. There are major gaps in the literature with respect to risk factors for the natural progression of hydrocephalus. Only two observational studies were included and three factors reported. Many risk factors for the onset of hydrocephalus have been studied; for most, evidence remains limited or inconclusive. More work is needed to confirm any causal associations and better inform policy."""
```

### Ejemplo 2

```
    Input:
"""TY  - JOUR
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

    Output:
"""http://www.epistemonikos.org/documents/0f8b5c48838a36541497f4d318c92297c3fa68e3	Chronic cough due to acute bronchitis: ACCP evidence-based clinical practice guidelines.	BACKGROUND: The purpose of this review is to present the evidence for the diagnosis and treatment of cough due to acute bronchitis and make recommendations that will be useful for clinical practice. Acute bronchitis is one of the most common diagnoses made by primary care clinicians and emergency department physicians. It is an acute respiratory infection with a normal chest radiograph that is manifested by cough with or without phlegm production that lasts for up to 3 weeks. Respiratory viruses appear to be the most common cause of acute bronchitis; however, the organism responsible is rarely identified in clinical practice because viral cultures and serologic assays are not routinely performed. Fewer than 10% of patients will have a bacterial infection diagnosed as the cause of bronchitis. The diagnosis of acute bronchitis should be made only when there is no clinical or radiographic evidence of pneumonia, and the common cold, acute asthma, or an exacerbation of COPD have been ruled out as the cause of cough. Acute bronchitis is a self-limited respiratory disorder, and when the cough persists for >3 weeks, other diagnoses must be considered.METHODS: Recommendations for this review were obtained from data using a National Library of Medicine (PubMed) search dating back to 1950, which was performed in August 2004. The search was limited to literature published in the English language and human studies, using search terms such as "cough," "acute bronchitis," and "acute viral respiratory infection."RESULTS: Unfortunately, most previous controlled trials guiding the treatment of acute bronchitis have not vigorously differentiated acute bronchitis and the common cold, and also have not distinguished between an acute exacerbation of chronic bronchitis and acute asthma as a cause of acute cough. For patients with the putative diagnosis of acute bronchitis, routine treatment with antibiotics is not justified and should not be offered. Antitussive agents are occasionally useful and can be offered as therapy for short-term symptomatic relief of coughing, but there is no role for inhaled bronchodilator or expectorant therapy. Children and adult patients with confirmed and probable whooping cough should receive a macrolide antibiotic and should be isolated for 5 days from the start of treatment; early treatment within the first few weeks will diminish the coughing paroxysms and prevent spread of the disease; the patient is unlikely to respond to treatment beyond this period.CONCLUSION: Acute bronchitis is an acute respiratory infection that is manifested by cough and, at times, sputum production that lasts for no more than 3 weeks. This syndrome should be distinguished from the common cold, an acute exacerbation of chronic bronchitis, and acute asthma as the cause of acute cough. The widespread use of antibiotics for the treatment of acute bronchitis is not justified, and vigorous efforts to curtail their use should be encouraged.
http://www.epistemonikos.org/documents/177eb71442d2ef8dcf2811559a3ff13314275b5e	Antibiotics for the common cold and acute purulent rhinitis.	BACKGROUND: It has long been believed that antibiotics have no role in the treatment of common colds yet they are often prescribed in the belief that they may prevent secondary bacterial infections. OBJECTIVES: To determine the efficacy of antibiotics compared with placebo for reducing general and specific nasopharyngeal symptoms of acute upper respiratory tract infections (URTIs) (common colds).To determine if antibiotics have any influence on the outcomes for acute purulent rhinitis and acute clear rhinitis lasting less than 10 days before the intervention.To determine whether there are significant adverse outcomes associated with antibiotic therapy for participants with a clinical diagnosis of acute URTI or acute purulent rhinitis. SEARCH METHODS: For this 2013 update we searched CENTRAL 2013, Issue 1, MEDLINE (March 2005 to February week 2, 2013), EMBASE (January 2010 to February 2013), CINAHL (2005 to February 2013), LILACS (2005 to February 2013) and Biosis Previews (2005 to February 2013). SELECTION CRITERIA: Randomised controlled trials (RCTs) comparing any antibiotic therapy against placebo in people with symptoms of acute upper respiratory tract infection for less than seven days, or acute purulent rhinitis less than 10 days in duration. DATA COLLECTION AND ANALYSIS: Both review authors independently assessed trial quality and extracted data. MAIN RESULTS: This updated review included 11 studies. Six studies contributed to one or more analyses related to the common cold, with up to 1047 participants. Five studies contributed to one or more analyses relating to purulent rhinitis, with up to 791 participants. One study contributed only to data on adverse events and one met the inclusion criteria but reported only summary statistics without providing any numerical data that could be included in the meta-analyses. Interpretation of the combined data is limited because some studies included only children, or only adults, or only males; a wide range of antibiotics were used and outcomes were measured in different ways. There was a moderate risk of bias because of unreported methods details or because an unknown number of participants were likely to have chest or sinus infections.Participants receiving antibiotics for the common cold did no better in terms of lack of cure or persistence of symptoms than those on placebo (risk ratio (RR) 0.95, 95% confidence interval (CI) 0.59 to 1.51, (random-effects)), based on a pooled analysis of six trials with a total of 1047 participants. The RR of adverse effects in the antibiotic group was 1.8, 95% CI 1.01 to 3.21, (random-effects). Adult participants had a significantly greater risk of adverse effects with antibiotics than with placebo (RR 2.62, 95% CI 1.32 to 5.18) (random-effects) while there was no greater risk in children (RR 0.91, 95% CI 0.51 to 1.63).The pooled RR for persisting acute purulent rhinitis with antibiotics compared to placebo was 0.73 (95% CI 0.47 to 1.13) (random-effects), based on four studies with 723 participants. There was an increase in adverse effects in the studies of antibiotics for acute purulent rhinitis (RR 1.46, 95% CI 1.10 to 1.94). AUTHORS' CONCLUSIONS: There is no evidence of benefit from antibiotics for the common cold or for persisting acute purulent rhinitis in children or adults. There is evidence that antibiotics cause significant adverse effects in adults when given for the common cold and in all ages when given for acute purulent rhinitis. Routine use of antibiotics for these conditions is not recommended."""
```

## 3.- Parsear expresión booleana

Esta prueba consiste en evaluar una expresión booleana representada en un string.
La expresión puede tener las siguientes formas:

- "t" se evalúa como True
- "f" se evalúa como False
- "!(expr)" se evalúa como NOT de la expresión que se encuentra dentro del paréntesis
- "&(expr1,expr2,...)" se evalúa como un AND de 2 o más expresiones que se encuentran dentro del paréntesis
- "|(expr1,expr2,...)" se evalúa como un OR de 2 o más expresiones que se encuentran dentro del paréntesis

### Ejemplo 1

```
    Input: "!(f)"
    Output: True
```

### Ejemplo 2

```
    Input: "&(t,t,f)"
    Output: False
```

### Ejemplo 3

```
    Input: "|(f,!(f))"
    Output: True
```

### Ejemplo 4

```
    Input: "|(!(t),&(t,f,t))"
    Output: False
```