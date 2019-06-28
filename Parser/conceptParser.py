import csv

def isSNOMEDOrRXDrug(row):
    return row['domain_id'] == 'Drug' and (row['vocabulary_id'] == 'SNOMED' or row['vocabulary_id'] == 'RxNorm')\
            and row['invalid_reason'] == ''

def filterConcepts(predicate):

    columns = ['concept_id', 'concept_name', 'domain_id', 'vocabulary_id', 'concept_class_id', 'standard_concept', 'concept_code',\
            'valid_start_date', 'valid_end_date', 'invalid_reason']
    
    concepts = {}

    with open('./CONCEPT.csv') as conceptFile:
        reader = csv.DictReader(conceptFile, delimiter='\t', quoting=csv.QUOTE_NONE)
        count = 0

        for row in reader:
            if predicate(row):
                concepts[row['concept_id']] = row['concept_name']

            count += 1
            if count % 1000000 == 0:
                print ('Finished filtering ' + str(count) + ' rows...')
        
        print('Finish filtering concept...')

