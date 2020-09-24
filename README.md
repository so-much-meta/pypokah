# pypokereval
Python poker evaluator

## Example

```python
In [0]: import pypokereval as pe

In [1]: handc1 = pe.getcards('th js')                                                                                                                                     

In [2]: handc1                                      
Out[2]: [35, 40]

In [3]: handc2 = pe.getcards('qd qs')                                      

In [4]: handc2                                                                                       
Out[4]: [42, 44]

In [5]: boardc = pe.getcards(['9h', 'Qc', 'Ks'])  # Accepts list of strings as well                                                                       

In [6]: boardc
Out[6]: [31, 41, 48]

In [7]: r1 = pe.eval5(handc1 + boardc) # Also see eval6, eval7, evalany                                                                    

In [8]: r2 = pe.eval5(handc2 + boardc)                                     

In [9]: pe.rankinfo(r1)                                     
Out[9]: {'type': 5, 'rank': 9, 'value': 20489, 'name': 'straight'}

In [10]: pe.rankinfo(r2)                                      
Out[10]: {'type': 4, 'rank': 713, 'value': 17097, 'name': 'three of a kind'}

In [11]: r1>r2                                      
Out[11]: True

In [12]: r1                                      
Out[12]: 20489

In [13]: r2                                   
Out[13]: 17097

In [14]: pe.gethand(boardc) # For consistency, cards means list of cards, hand means human-readable string                                                                                                      
Out[14]: '9h Qc Ks'

In [15]: pe.gethand(boardc, compress=True)                  
Out[15]: '9hQcKs'
```

## INSTALL
```
# Or just util extras (parse training games, run lczero engine, etc)
pip install git+https://github.com/gomolot/pypokereval.git

# Or from source tree...
git clone https://github.com/gomolot/pypokereval
cd pypokereval
# Note: Creating and using a virtualenv or Conda environment before install is suggested, as always
pip install .
# Or for developer/editable install, to make in place changes:
# pip install -e .
```
