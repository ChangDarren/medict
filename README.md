# Medict
Medict is a mini-project created in NUHS for mapping a given drug name to a drug name in the OMOP concept database. It is a project created to help with the data migration from the local database(datamart) to OMOP. To reduce the hassle of usage within the local virtual environment of the hospital system, one of the key criteria of Medict is that it uses only local python library and no other import is required. 

## Usage:
`Usage: python3 main.py <input_file_name> <output_file_name>`

## Note:
`input_file` should contain a list of the name of drugs that one is interested in mapping. For e.g.
>Omeprazole 2mg/mL
> Paracetemol
> Paracetemol 500g
> Ferusemide 4mg/mL
> .
> .
> .

`output_file` will contain the result which is a list of the given name, the OMOP drug name it gets mapped to and the OMOP concept ID

## Details:
* The main assumption that the algorithm holds is that similar drug names represents the same drug as such, the goal at hand is to find the most similar string in the concept file to the given drug name in the system.

### Implementation:
Given the drug name that we want to match, there are 2 main steps namely:

1. Reducing the possible words that could possibly match the given drug name
2. Find the closest matching word - Levenshtein distance between the word is used here after removing some common words.

 In order to solve the first problem, a Trie with adjustable path is employed. The path of the trie is modified compared to a typical trie as medicine names have certain heuristics that allow us to better narrow down the search space such as the fact that concentration often comes after the name of the drug. The path can be adjusted by altering the function `__getPathWord(self, newWord)`.
 
### Use Case
 
 Below is a use case to explain how the Trie is being used:
 
 Suppose we have the following Trie, 
 
  `P` -> `A` -> `N` -> `A` -> `D` -> `O` -> `L` -> `5` -> `0` -> `0` -> `M` -> `G`
  
  where the string "Panadol 500mg" is in the G node.
 
 1. The drug name in the local system is "Panadol 625mg". We will trace through the trie until we hit the first letter that does not match. In this case, it would be `5`. 
 2. From `L`, we will do a BFS to gather all the concept name that is after the path of PANADOL.
 3. Among all the possible concepts, we will compare with the drug name and get the concept with the least word distance and is below the `threshold`. If no such concept exists, 0 will be put to signify no concept is found.
 