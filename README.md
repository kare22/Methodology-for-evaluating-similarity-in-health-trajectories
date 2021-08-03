Antud skript on loodud Tartu Ülikooli lõputöö raames teemal **Haigustrajektooride sarnasuse hindamise metoodika**.
Töö eesmärgiks on leida sarnaseid haigustrajektoore etteantud patsientide diagnooside trajektooride hulgast.

## Autor
	Karel Paan, Tartu Ülikool

# Methodology for evaluating similarity in health trajectories
The following work consists of a method for finding most similar health trajectories within a give set of data.

[Data](./diagnoses.csv) used for this analyzes was created by using a generator which was made by [Artjom Valdas].
Trajectories that are brought out in [trajectories.py](./trajectories.py) are taken from said work.

The main functionality exists in [main.ipynb](./main.ipynb). It also consists of functions for analyzing the result. To fit the given model, one should place the code within a loop.

The local alignment implementation can be found in
[local_alignment.py](./local_alignment.py).



[Artjom Valdas]: https://github.com/valart/diagnoses-synthesis