from selenium.webdriver.common.by import By

class AdminPageLocators():
    name_field = (By.ID, "nom")
    email_field = (By.ID, "mail")
    isc_toggle = (By.ID, "ics")
    isc_field = (By.ID, "ics")

    author_field = (By.ID, "comment")
    comment_field = (By.ID, "commentdesc")
    add_comment_btn = (By.XPATH, "//p-button[@label='Ajouter commentaire']")
    vue_table_btn = (By.CLASS_NAME, "pi-table")

    agenda_flux_switch = (By.XPATH, "//p-inputSwitch/*[1]")

    pref_alimentaire_switch = (By.XPATH, "//p-inputSwitch/*[2]")

    vue_table_btn = (By.CLASS_NAME, "pi-table")

    vue_calendar_btn = (By.CLASS_NAME, "pi-calendar")

    author_cmt_field = (By.ID, "comment")

    cmt_content_field = (By.ID, "commentdesc")

    add_cmt_btn = (By.XPATH, "//p-button[@label='Ajouter commentaire']")

    th_tag = (By.TAG_NAME, "th")
    tr_tag = (By.TAG_NAME, "tr")
    td_tag = (By.TAG_NAME, "td")




    #nameInput = BasePageElement((By.ID, "nom"))
    #_emailInput = (By.ID, "mail")
    #_iscToggle = (By.ID, "ics")
    #_fisrtToggle = (By.XPATH, "//p-inputSwitch[@ng-reflect-model='hasics']")
    #_secondToggle = (By.XPATH, "//p-inputSwitch[@ng-reflect-model='personalInformation.pref']")
    #_authorComment = (By.ID, "comment")
    #_comment = (By.ID, "commentdesc")
    #_addComment = (By.XPATH, "//p-button[@label='Ajouter commentaire']")
    #_newLink = (By.XPATH, "//a[text()='nouveau']")
    #_shareLink = (By.XPATH, "//a[text()='Partager']")
    #_vueTableau = (By.CLASS_NAME, "pi-table")