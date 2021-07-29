import time
import subprocess
from tqdm.auto import tqdm



def say(text):
    """ Говорит человеческим языком  """
    subprocess.call(['say', text])



s = """
Бедов Роман Вячеславович <Bedov.Ro.Vy@sberbank.ru>,
Мелихова Елена Борисовна <Melikhova.E.Bo@sberbank.ru>,
Ахмадеев Марат Айдарович <Akhmadeev.Ma.Ay@sberbank.ru>,
Канеев Рафаэль Шамильевич <Kaneev.R.S@sberbank.ru>,
Крыцын Никита Алексеевич {ДВ} <Krytsyn.N.Al@omega.sbrf.ru>,
Земляков Алексей Юрьевич {ПЦП} <Zemlyakov.A.Y@omega.sbrf.ru>,
Васильев Станислав Андреевич <Vasilyev.St.An1@sberbank.ru>,
Наумов Евгений Николаевич {СЗБ} <Naumov.E.Ni@omega.sbrf.ru>,
Кобринский Андрей Владиславович {ЦА} <Kobrinskiy.An.Vl@omega.sbrf.ru>,
Кобринский Андрей Владиславович <kobrinskiy-av@sberbank.ru>,
Исайкова Наталья Сергеевна - СИБ <Isaykova.N.S@sberbank.ru>,
Янов Роман Андреевич {МБ} <Yanov.R.A@omega.sbrf.ru>,
Янов Роман Андреевич <Yanov.R.A@sberbank.ru>,
Баер Михаил Дмитриевич <Baer.M.D@sberbank.ru>,
Климкин Кирилл Валерьевич {ПЦП} <Klimkin.K.Va@omega.sbrf.ru>,
Берняева Ирина Юрьевна {ДВБ} <Bernyaeva.Ir.Yu@omega.sbrf.ru>,
Рыбалко Любовь Сергеевна - СРБ <lsrybalko@sberbank.ru>,
Лось Екатерина Андреевна {УРАЛ} <EALos@omega.sbrf.ru>,
Матясова Людмила Геннадьевна {СИБ} <Matyasova.Ly.Ge@omega.sbrf.ru>,
Куликова Наталия Владимировна {МБ} <Kulikova.N.V@omega.sbrf.ru>,
Мешавкина Ольга Викторовна - УБ <ovmeshavkina@sberbank.ru>,
Анисимова Мария Николаевна {МБ} <Anisimova.M.N@omega.sbrf.ru>,
Аристов Евгений Вадимович {СЗБ} <Aristov.Ev.Va@omega.sbrf.ru>,
Давыдова Екатерина Геннадьевна {ББ} <Davydova.Ek.Ge1@omega.sbrf.ru>,
Римойал Джим Абел {ЮЗБ} <Rimoyal.Dz.Ab@omega.sbrf.ru>,
Бенбера Евгений Васильевич {ЮЗБ} <Benbera.Ev.Va@omega.sbrf.ru>,
Земсков Савелий Кириллович {МБ} <SKiZemskov@omega.sbrf.ru>,
Земсков Савелий Кириллович <SKiZemskov@sberbank.ru>,
Нафикова Луиза Рашитовна {УРАЛ} <Nafikova.Lu.R@omega.sbrf.ru>,
Нафикова Луиза Рашитовна - УБ <lrnafikova@sberbank.ru>,
Романова Мария Николаевна {УРАЛ} <Romanova.Ma.N@omega.sbrf.ru>,
Романова Мария Николаевна - УБ <manromanova@sberbank.ru>,
Елохина Светлана Владимировна {УРАЛ} <Elokhina.Sv.V@omega.sbrf.ru>,
Солодовникова Мария Викторовна {УРАЛ} <Solodovnikova.Ma.V@omega.sbrf.ru>,
Кабакова Екатерина Павловна {МБ} <Kabakova.E.P@omega.sbrf.ru>,
Гарибян Артур Мартиросович <AMGaribyan@sberbank.ru>,
Иванцов Кирилл Александрович <Ivantsov.K.Al@sberbank.ru>
"""

if __name__ == "__main__":
    say('Проверка связи! Раз-Раз ...')
    time.sleep(30)
    time_space = 30
    s = s.split(",")
    s = [' '.join(x.split(' ')[:3]) for x in s]
    s = [x.strip('\n') for x in s]
    s = list(set([' '.join([x.split(' ')[1], x.split(' ')[0]]) for x in s]))
    for name in tqdm(s):
        print(name)
        say(name)

        print('_' * 30)
        for _ in tqdm(range(time_space)):
            time.sleep(1)
        else:
            say(f'Спасибо {name.split()[0]}')
