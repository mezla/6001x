def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposureBad(start, stop, step):
    '''
    greska: kod svake iteracije treba rezultat f(start) pomnoziti sa step
    da bi se dobila povrsina, a zbroj svih povrsina je rjesenje
    ja ovdje na kraju pomnozim ukupan rezultat sa step da bi dobio ispravnu
    povrsinu ako step nije 1, sto nije bas najbolji nacin.
    '''
    try:
        exposure
    except NameError:
        global exposure
        exposure = 0.0
    
    if start >= stop:
        res = exposure
        exposure = 0.0
        if step != 1:
            return res*step
        else:
            return res
    else:
        exposure += f(start)
        return radiationExposureBad(start+step, stop, step)

def radiationExposureGood(start, stop, step):
    '''
    ovdje ispravo vracam povrsinu u svakoj iteraciji, a dodatno sam se rjesio
    varijable koja cuva rezultat jer je u rekurzivnim funkcijama nepotrebna
    rjesenje se vraca kao povrsina + ponovni_poziv_funkcije ili samo povrsina
    ako smo dosli do kraja - u tome slucaju se rezultati pocnu "urusavati" dok
    se ne dodje do izvorne funkcije koja vrati rezultat
    python tutor vizualizacija ovdje moze pomoci
    '''
    if start+step >= stop:
        return f(start)*step
    else:
        return f(start)*step + radiationExposureGood(start+step, stop, step)
