# rc-tools

[![Build Status](https://travis-ci.org/fmassot/rc-tools.svg)](https://travis-ci.org/fmassot/rc-tools)

## Install :
```bash
pip instal -r requirements.txt
```

## Launch tests :

```bash
python -m unittest discover
```

## Commands :

### Assemblee nationale

* Show a amendement given its url :

```python
python assemblee_nationale/manage.py show_amendement http://www.assemblee-nationale.fr/14/amendements/1847/CION-DVP/CD266.asp
```

* Print amendements order for a given id_dossier and id_examen :

```python
python assemblee_nationale/manage.py show_amendements_order 33299 4073
```

* Show some amdements after a given date :
```python
python assemblee_nationale/manage.py show_amendements 2014-06-01
```

### Nosdeputes

 * Print and save in missing_urls.txt amendements which are not in nosdeputes database :

```python
python nosdeputes/manage.py check_if_amendement_are_in_db 2012-01-01 --end-date 2015-01-01
```

 * Make liasse of a given texteloi_id : 

```python
python nosdeputes/manage.py make_liasse 2173
```
