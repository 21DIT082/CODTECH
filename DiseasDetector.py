disease_data = {
    "Common Cold": ["cough", "sore throat", "runny nose", "congestion", "sneezing"],
    "Flu": ["fever", "chills", "muscle aches", "cough", "congestion", "fatigue"],
    "COVID-19": ["fever", "cough", "shortness of breath", "fatigue", "loss of taste", "loss of smell"],
    "Strep Throat": ["sore throat", "fever", "swollen lymph nodes", "red spots in the mouth"],
    "Allergies": ["sneezing", "runny nose", "itchy eyes", "congestion", "cough"],
    "Asthma": ["wheezing", "shortness of breath", "chest tightness", "coughing"],
    "Bronchitis": ["cough", "mucus production", "fatigue", "shortness of breath", "chest discomfort"],
    "Pneumonia": ["chest pain", "cough", "fever", "chills", "shortness of breath"],
    "Migraine": ["headache", "nausea", "vomiting", "sensitivity to light", "sensitivity to sound"],
    "Sinusitis": ["facial pain", "nasal congestion", "runny nose", "loss of smell", "cough"],
    "Gastroenteritis": ["diarrhea", "nausea", "vomiting", "abdominal pain", "fever"],
    "Chickenpox": ["rash", "fever", "tiredness", "loss of appetite", "headache"],
    "Measles": ["rash", "fever", "cough", "runny nose", "red eyes"],
    "Mumps": ["swollen glands", "fever", "headache", "muscle aches", "fatigue"],
    "Mononucleosis": ["fever", "sore throat", "swollen lymph nodes", "fatigue", "muscle aches"],
    "Tuberculosis": ["persistent cough", "chest pain", "weight loss", "fatigue", "fever"],
    "Lyme Disease": ["rash", "fever", "chills", "fatigue", "muscle aches"],
    "Hepatitis A": ["fatigue", "nausea", "abdominal pain", "loss of appetite", "fever"],
    "Hepatitis B": ["fatigue", "abdominal pain", "loss of appetite", "nausea", "joint pain"],
    "Hepatitis C": ["fatigue", "fever", "nausea", "vomiting", "abdominal pain"],
    "Malaria": ["fever", "chills", "headache", "sweating", "muscle pain"],
    "Dengue Fever": ["fever", "rash", "headache", "joint pain", "muscle pain"],
    "Zika Virus": ["fever", "rash", "joint pain", "red eyes", "muscle pain"],
    "Ebola Virus": ["fever", "severe headache", "muscle pain", "weakness", "diarrhea"],
    "Rabies": ["fever", "headache", "nausea", "vomiting", "agitation"],
    "Tetanus": ["muscle stiffness", "difficulty swallowing", "jaw cramping", "seizures", "fever"],
    "Meningitis": ["fever", "headache", "stiff neck", "nausea", "sensitivity to light"],
    "Encephalitis": ["fever", "headache", "confusion", "seizures", "fatigue"],
    "Sepsis": ["fever", "difficulty breathing", "low blood pressure", "fast heart rate", "confusion"],
    "Hypertension": ["headache", "dizziness", "blurred vision", "chest pain", "shortness of breath"],
    "Diabetes": ["increased thirst", "frequent urination", "hunger", "fatigue", "blurred vision"],
    "Hyperthyroidism": ["weight loss", "rapid heartbeat", "nervousness", "sweating", "tremors"],
    "Hypothyroidism": ["fatigue", "weight gain", "cold intolerance", "constipation", "dry skin"],
    "Lupus": ["fatigue", "joint pain", "rash", "fever", "swelling"],
    "Rheumatoid Arthritis": ["joint pain", "swelling", "stiffness", "fatigue", "fever"],
    "Multiple Sclerosis": ["fatigue", "numbness", "vision problems", "muscle weakness", "dizziness"],
    "Parkinson's Disease": ["tremors", "slowed movement", "muscle stiffness", "balance problems", "speech changes"],
    "Alzheimer's Disease": ["memory loss", "confusion", "difficulty completing tasks", "changes in mood", "disorientation"],
    "Chronic Fatigue Syndrome": ["fatigue", "sore throat", "headache", "muscle pain", "joint pain"],
    "Fibromyalgia": ["widespread pain", "fatigue", "sleep problems", "memory issues", "mood issues"],
    "Irritable Bowel Syndrome": ["abdominal pain", "cramping", "bloating", "gas", "diarrhea", "constipation"],
    "Celiac Disease": ["diarrhea", "bloating", "gas", "fatigue", "weight loss"],
    "Crohn's Disease": ["diarrhea", "abdominal pain", "fatigue", "weight loss", "malnutrition"],
    "Ulcerative Colitis": ["diarrhea", "abdominal pain", "rectal bleeding", "fatigue", "weight loss"],
    "Peptic Ulcer": ["abdominal pain", "bloating", "heartburn", "nausea", "vomiting"],
    "Gastritis": ["abdominal pain", "nausea", "vomiting", "bloating", "loss of appetite"],
    "Gallstones": ["abdominal pain", "nausea", "vomiting", "bloating", "indigestion"],
    "Kidney Stones": ["severe pain", "nausea", "vomiting", "urinary urgency", "blood in urine"],
    "Urinary Tract Infection": ["burning sensation when urinating", "frequent urination", "cloudy urine", "pelvic pain", "fever"],
    "Prostatitis": ["painful urination", "difficulty urinating", "pelvic pain", "flu-like symptoms", "fever"],
    "Eczema": ["itchy skin", "red patches", "dry skin", "cracked skin", "swelling"],
    "Psoriasis": ["red patches", "scales", "dry skin", "itching", "burning"],
    "Cellulitis": ["red area of skin", "swelling", "pain", "warmth", "fever"],
    "Shingles": ["pain", "rash", "blisters", "itching", "fever"],
    "Chickenpox": ["rash", "fever", "tiredness", "loss of appetite", "headache"],
    "Measles": ["rash", "fever", "cough", "runny nose", "red eyes"],
    "Mumps": ["swollen glands", "fever", "headache", "muscle aches", "fatigue"],
    "Rubella": ["rash", "fever", "swollen lymph nodes", "red eyes", "runny nose"],
    "Whooping Cough": ["severe cough", "runny nose", "nasal congestion", "red eyes", "fever"],
    "Diphtheria": ["sore throat", "fever", "swollen glands", "weakness", "difficulty breathing"],
    "Tonsillitis": ["sore throat", "red tonsils", "white patches on tonsils", "fever", "difficulty swallowing"],
    "Pharyngitis": ["sore throat", "fever", "headache", "swollen lymph nodes", "fatigue"],
    "Laryngitis": ["hoarse voice", "sore throat", "dry throat", "dry cough", "tickling sensation in throat"],
    "Epiglottitis": ["severe sore throat", "fever", "difficulty swallowing", "drooling", "difficulty breathing"],
    "Croup": ["barking cough", "hoarseness", "fever", "difficulty breathing", "stridor"],
    "Bronchiolitis": ["cough", "wheezing", "difficulty breathing", "fever", "runny nose"],
    "Pulmonary Embolism": ["shortness of breath", "chest pain", "cough", "rapid heart rate", "dizziness"],
    "Deep Vein Thrombosis": ["swelling", "pain", "redness", "warmth", "leg cramps"],
    "Heart Attack": ["chest pain", "shortness of breath", "nausea", "lightheadedness", "pain in arm or shoulder"],
    "Stroke": ["sudden numbness", "confusion", "trouble speaking", "vision problems", "trouble walking"],
    "Aneurysm": ["sudden severe headache", "nausea", "vision impairment", "seizure", "loss of consciousness"],
    "Cardiomyopathy": ["shortness of breath", "fatigue", "swelling in legs", "rapid heartbeat", "dizziness"],
    "Congestive Heart Failure": ["shortness of breath", "fatigue", "swelling in legs", "rapid heartbeat", "persistent cough"],
    "Peripheral Artery Disease": ["leg pain", "leg numbness", "coldness in lower leg", "sores on toes", "shiny skin"],
    "Varicose Veins": ["dark purple veins", "bulging veins", "aching pain", "itching", "swelling"],
    "Thyroid Cancer": ["lump in neck", "difficulty swallowing", "hoarseness", "swollen lymph nodes", "neck pain"],
    "Breast Cancer": ["lump in breast", "change in breast shape", "nipple discharge", "breast pain", "swelling in armpit"],
    "Lung Cancer": ["persistent cough", "coughing up blood", "chest pain", "hoarseness", "weight loss"],
    "Colon Cancer": ["change in bowel habits", "rectal bleeding", "abdominal pain", "fatigue", "weight loss"],
    "Prostate Cancer": ["difficulty urinating", "blood in urine", "pelvic pain", "bone pain", "erectile dysfunction"],
    "Leukemia": ["fever", "fatigue", "frequent infections", "easy bruising", "weight loss"],
    "Lymphoma": ["swollen lymph nodes", "fatigue", "fever", "night sweats", "unexplained weight loss"],
    "Skin Cancer": ["new mole", "change in existing mole", "skin lesion", "itching", "bleeding"],
    "Pancreatic Cancer": ["abdominal pain", "weight loss", "jaundice", "loss of appetite", "nausea"],
    "Ovarian Cancer": ["abdominal pain", "bloating", "frequent urination", "loss of appetite", "fatigue"],
    "Kidney Cancer": ["blood in urine", "back pain", "weight loss", "fatigue", "fever"],
    "Bladder Cancer": ["blood in urine", "painful urination", "frequent urination", "back pain", "pelvic pain"],
    "Esophageal Cancer": ["difficulty swallowing", "chest pain", "weight loss", "hoarseness", "cough"],
    "Stomach Cancer": ["abdominal pain", "nausea", "weight loss", "difficulty swallowing", "vomiting blood"],
    "Brain Cancer": ["headache", "seizures", "nausea", "vision problems", "behavior changes"],
    "Bone Cancer": ["bone pain", "swelling", "fractures", "fatigue", "weight loss"],
    "Multiple Myeloma": ["bone pain", "nausea", "fatigue", "frequent infections", "weight loss"],
}


def get_user_symptoms():
    symptoms = input("Enter your symptoms separated by commas: ")
    return [symptom.strip().lower() for symptom in symptoms.split(",")]


def detect_disease(user_symptoms):
    possible_diseases = {}
    
    for disease, symptoms in disease_data.items():
        match_count = len(set(user_symptoms) & set(symptoms))
        if match_count > 0:
            possible_diseases[disease] = match_count
    
    if possible_diseases:
        sorted_diseases = sorted(possible_diseases.items(), key=lambda item: item[1], reverse=True)
        return sorted_diseases
    else:
        return None


def display_results(possible_diseases):
    if possible_diseases:
        print("Based on your symptoms, you might have the following diseases:")
        for disease, count in possible_diseases:
            print(f"- {disease} (matching symptoms: {count})")
    else:
        print("No diseases found matching your symptoms. Please consult a healthcare professional for accurate diagnosis.")


def main():
    user_symptoms = get_user_symptoms()
    possible_diseases = detect_disease(user_symptoms)
    display_results(possible_diseases)


if __name__ == "__main__":
    main()
