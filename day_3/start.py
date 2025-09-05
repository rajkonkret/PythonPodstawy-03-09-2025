import pakiet

# pakiet pozwala sterować widocznościa elementów
# w katalogu wszystkie są widoczne

# AttributeError: module 'pakiet' has no attribute 'powitanie'
# pakiet.powitanie()
pakiet.info()  # info działa bo jest w __all__
# Jestem pakietem

from pakiet import fun  # import konkretnego pliku

fun.powitanie() # Powitanie

import pakiet.fun as pk  # import jako alias

pk.powitanie() # Powitanie
