def este_isograma(text: str) -> str:
    filtrat = text.replace(" ", "").lower()
    if len(set(filtrat)) == len(filtrat):
        return f"'{text}' este isogramă."
    else:
        return f'\'{text}\' NU este isogramă.'
