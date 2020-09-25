# pypokereval
Python poker evaluator

## Example

```python
>>> import pypokah as pok

>>> handc1 = pok.getcards('th js')

>>> handc1
[35, 40]

>>> handc2 = pok.getcards('qd qs')                                      

>>> handc2                                                                                       
[42, 44]

>>> boardc = pok.getcards(['9h', 'Qc', 'Ks'])  # Accepts list of strings as well                                                                       

>>> boardc
[31, 41, 48]

>>> r1 = pok.eval5(handc1 + boardc) # Also see eval6, eval7, evalany                                                                    

>>> r2 = pok.eval5(handc2 + boardc)                                     

>>> pok.rankinfo(r1)                                     
{'type': 5, 'rank': 9, 'value': 20489, 'name': 'straight'}

>>> pok.rankinfo(r2)                                      
{'type': 4, 'rank': 713, 'value': 17097, 'name': 'three of a kind'}

>>> r1>r2                                      
True

>>> r1                                      
20489

>>> r2                                   
17097

>>> pok.gethand(boardc) # For consistency, cards means list of cards, hand means human-readable string                                                                                                      
'9h Qc Ks'

>>> pok.gethand(boardc, compress=True)                  
'9hQcKs'
```

## INSTALL
```
# over http
pip install git+https://github.com/gomolot/pypokereval.git

# Or from source tree...
git clone https://github.com/gomolot/pypokereval
cd pypokereval

# Note: Creating and using a virtualenv or Conda environment before install is suggested, as always
pip install .
# Or for developer/editable install, to make in place changes:
# pip install -e .
```
