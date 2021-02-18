import postinumerot


def test_keravan_postitoimipaikka():
    tulos = postinumerot.etsi_numerot('KERAVA')

    assert tulos == "Postinumerot: 04200, 04201, 04220, 04230, 04250, 04251, 04260, 04261"

def test_kerkonjoensuun_postitoimipaikka():
    tulos = postinumerot.etsi_numerot('KERKONJOENSUU')

    assert tulos == "Postinumerot: 77930"
    
def test_paikka_jota_ei_ole():
    tulos = postinumerot.etsi_numerot('CHIGAGO')

    assert tulos == "Toimipaikkaa ei löytynyt"

def test_smartpost_bugi():
    tulos = postinumerot.etsi_numerot('SMART POST')
    shouldBe = postinumerot.etsi_numerot('SMARTPOST')
    assert tulos == shouldBe
