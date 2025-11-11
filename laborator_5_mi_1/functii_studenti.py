if __name__ == '__main__':
    def timp_in_format(secunde: int) -> str:
        if secunde<0:
            return "Eroare: numărul de secunde trebuie să fie nenegativ."
        ore=secunde//3600
        minute=(secunde%3600)//60
        secunde_ramase=secunde%60
        hh=f"{ore:02d}"
        mm=f"{minute:02d}"
        ss=f"{secunde_ramase:02d}"
        timp_format=f"{hh}:{mm}:{ss}"
        return f"{secunde} secunde inseamna {timp_format}."