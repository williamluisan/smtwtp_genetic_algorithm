
# Single Machine Total Weighted Tardiness Problem

Alright, this python code is purposed to solve SMTWTP 
(Single Machine Total Weighted Tardiness Problem) using
Genetic Algorithm.

## Genetic Algorithm in this project
You can take a look the GA implemented inside a file: `genetic_algorithm.py`

On this project, this is how the GA mechanism works:
1. Generate Random Solutions
* Firstly, this program will take a SMTWTP problem as an input from an excel file: `data/case_1.xls` (usual SMTWTP problem table)
* and will generate random solutions of the given problem
* the first solutions generated are 6 in total (why 6? because following the total of the projects)
2. Calculate Fitness Function
* calculating the fitness function (total weighted tardiness) as per SMTWTP formula
3. Selection Process
* the selection process will take two chromosomes as parents randomly and prepared for crossover
* after selecting the parents, the crossover is executed. After the crossover, this program will sort the 2 best candidate (chromosome) and will be the next gen candidate, this method is called as "Elitism"
4. Crossover Process
* in this process the parent's gene will be swapped to each other
* the genes that swapped are the last two genes of the parents. Can see the example on the table below
    Example | Chromsome
    --------|--------
    Chromosome A: | A F D C (B E)
    Chromosome B: | C A B F (E D)
    New Chromosome 1: | A F D C E D
    New Chromosome 2: | C A B F B E
 
5. Mutation Process
* mutation process will take a look if there's a same gene in a chromosome
* if there's a same gene, one of it will be replaced to a new unique gene which hasn't in the chromosome
    Example | Chromsome
    --------|--------
    New Chromosome 1: | A F D C E D
    New Chromosome 1 (mutated): | A F D C E B
    New Chromosome 2: | C A B F B E
    New Chromosome 2 (mutated): | C A B F D E



## Input & Ouput
* The program input as stated above is from the excel file `data/case_1.xls`
![picture alt](https://raw.githubusercontent.com/williamluisan/smtwtp_genetic_algorithm/master/screenshots/excel_input.png?token=GHSAT0AAAAAABVJJSZLVF746KPGB362Q5ICYU6BNYA "Input from Excel file")
* Expected output in terminal:
![picture alt](https://raw.githubusercontent.com/williamluisan/smtwtp_genetic_algorithm/master/screenshots/output.png?token=GHSAT0AAAAAABVJJSZKK3SFMXE7ALYNPZFQYU6BPKQ "Expected output")
## The Files
* `main.py`
* `data/case_1.xls`
* `genetic_algorithm.py`
* `helper.py`
* Just ignore the others
## Usage

```python
python main.py
```

