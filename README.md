# pypokereval
Python poker evaluator

## Example

```python
In [1]: hand1 = pe.getcards('th js')                                                                                                                                     

In [2]: hand1                                                                                                                                                            
Out[2]: [35, 40]

In [3]: hand2 = pe.getcards('qd qs')                                                                                                                                     

In [4]: hand2                                                                                                                                                            
Out[4]: [42, 44]

In [5]: board = pe.getcards(['9h', 'Qc', 'Ks'])  # Accepts list of strings as well                                                                                                                        

In [6]: board                                                                                                                                                            
Out[6]: [31, 41, 48]

In [7]: r1 = pe.eval5(hand1 + board) # Also see eval6, eval7, evalany                                                                                                                                   

In [8]: r2 = pe.eval5(hand2 + board)                                                                                                                                     

In [9]: pe.rankinfo(r1)                                                                                                                                                  
Out[9]: {'handType': 5, 'handRank': 9, 'value': 20489, 'handName': 'straight'}

In [10]: pe.rankinfo(r2)                                                                                                                                                  
Out[10]: {'handType': 4, 'handRank': 713, 'value': 17097, 'handName': 'three of a kind'}

In [11]: r1>r2                                                                                                                                                            
Out[11]: True

In [26]: r1                                                                                                                                                               
Out[26]: 20489

In [26]: r2                                                                                                                                                            
Out[26]: 17097
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
