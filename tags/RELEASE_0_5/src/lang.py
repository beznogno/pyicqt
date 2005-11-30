# -*- coding: UTF-8 -*-

import config

def get(lang=config.lang):
	if(not lang.__class__ in [str, unicode]):
		lang = config.lang
	try:
		lang = lang.replace("-", "_")
		return strings.__dict__[lang]
	except KeyError:
		return strings.__dict__[config.lang]


# If you change or add any strings in this file please contact the translators listed below
# Everything must be in UTF-8
# Look for language codes here - http://www.w3.org/WAI/ER/IG/ert/iso639.htm

class strings:
	class en: # English - James Bunton <mailto:james@delx.cjb.net>/Daniel Henninger <mailto:jadestorm@nc.rr.com>
		# Text that may get sent to the user. Useful for translations. Keep any %s symbols you see or you will have troubles later
		sessionGreeting = u"This is an experimental gateway, PyICQ-t. If you experience problems please contact Daniel Henninger <jadestorm@nc.rr.com>"
		registerText = u"Please type your ICQ user id number into the username field and your password."
		notLoggedIn = u"Error. You must log into the transport before sending messages."
		notRegistered = u"Sorry. You do not appear to be registered with this transport. Please register and try again. If you are having trouble registering please contact your Jabber administrator."
		waitForLogin = u"Sorry, this message cannot be delivered yet. Please try again when the transport has finished logging in."
		groupchatInvite = u"You have been invited into a groupchat on the legacy service. You must join this room to switch into groupchat mode %s.\nIf you do not join this room you will not be able to participate in the groupchat, but you will still appear to have joined it to contacts on the ICQ service."
		groupchatFailJoin1 = u"You did not join the groupchat room %s.\nThe following users were in the groupchat:"
		groupchatFailJoin2 = u"You have been removed from this room on the legacy service. The following was said before you were disconnected, while you appeared to be in the groupchat to the contacts on the legacy service."
		groupchatPrivateError = u"Sorry. You cannot send private messages to users in this groupchat. Please instead add the user to your contact list and message them that way."
		gatewayTranslator = u"Enter the user's ICQ user id number."
	en_US = en # en-US is the same as en, so are the others
	en_AU = en
	en_GB = en

	class de: # German - Windapple (Windapple@arcor.de)
		sessiongreeting = u"Dies ist ein experimentelles Gateway, PyICQ-t. Sollten Sie Probleme haben, bitte kontaktieren Sie Daniel Henninger <jadestorm@nc.rr.com>"
		registertext = u"Bitte geben Sie Ihre ICQ Nummer in das Benutzernamen-Feld und Ihr Passwort ein."
		notloggedin = u"Fehler. Sie müssen sich erst beim Transport anmelden bevor Nachrichten versendet werden können."
		notregistered = u"Es tut mir leid, aber Sie scheinen nicht bei diesem Transport registriert zu sein. Registrieren Sie sich bitte und versuchen sie es später noch einmal. Sollten Sie Probleme mit der Registrierung haben, bitte Kontaktieren Sie ihren Jabber Administrator."
		waitforlogin = u"Es tut mir leid, aber diese Nachricht kann jetzt noch nicht versendet werden. Versuchen Sie es nochmals wenn die Anmeldung beim Transport zuende geführt wurde."
		groupchatinvite = u"Sie wurden in einen Gruppenchat auf dem Legacy Service eingeladen. Sie müssen diesem Raum beitreten um in den Gruppenchat-Modus %s zu wechseln.\\nFalls Sie nicht diesem Raum beitreten werden Sie nicht am Gruppenchat teilnehmen können, aber den Kontakten auf dem ICQ Service wird suggeriert, Sie wären beigetreten. "
		groupchatfailjoin2 = u"Sie sind dem Gruppenchat-Raum %s nicht beigetreten.\\nDie folgenden Benutzer waren im Gruppenchat:"
		groupchatfailjoin2 = u"Sie wurden von diesem Raum auf dem Legacy Service entfernt. Das folgende wurde kurz vor dem Trennen gesagt, während Sie den Kontakten am Legace Service noch als im Gruppenchat Anwesend angezeigt wurden."
		groupchatprivateerror = u"Es tut mir leid, aber Sie können den Nutzern in diesem Gruppenchat keine Privaten Nachrichten senden. Bitte fügen Sie sie stattdessen Ihrer Kontakliste hinzu und senden Sie die Nachrichten auf diesem Wege."
		gatewaytranslator = u"Geben Sie die ICQ Nummer des Benutzers an."

	class pl: # Polish - Tomasz Dominikowski (dominikowski@gmail.com)
		sessiongreeting = u"To jest eksperymentalny transport, PyICQ-t. Jeśli występują problemy proszę skontaktować się z Danielem Henningerem <jadestorm@nc.rr.com>"
		registertext = u"Proszę podaj swój numer ICQ w polu nazwa_użytkownika oraz swoje hasło. "
		notloggedin = u"Błąd. Musisz zalogować się do transportu zanim rozpoczniesz wysyłanie wiadomości."
		notregistered = u"Wybacz, ale wygląda na to, że nie jesteś zarejestrowany w tym transporcie. Proszę zarejestruj się i spróbuj ponownie. Jeśli masz z rejestracją problemy skontaktuj się ze swoim administratorem Jabbera."
		waitforlogin = u"Wybacz, ta wiadomość nie może zostać dostarczona. Proszę spróbuj ponownie po zalogowaniu do transportu."
		groupchatinvite = u"Zostałeś zaproszony do grupowej rozmowy na zewnętrznej usłudze. Musisz dołączyć do pokoju aby wejść w tryb grupowej rozmowy %s.\\nJeśli nie dołączysz do pokoju nie będziesz mógł uczestniczyć w rozmowie grupowej, ale nadal będzie wyglądało, że dołączyłeś ten pokój do kontaktów w usłudze ICQ."
		groupchatfailjoin1 = u"Nie dołączyłeś do pokoju rozmowy grupowej %s.\\nW pokoju znajdowali się następujący użytkownicy:"
		groupchatfailjoin2 = u"Zostałeś usunięty z tego pokoju na zewnętrznej usłudze. Następująca treść została przekazana zanim zostałeś rozłączony, ale nadal widoczny w rozmowie grupowej na zewnętrznej usłudze."
		groupchatprivateerror = u"Wybacz, nie możesz wysłać prywatnej wiadomości do użytkowników rozmowy grupowej. Zamiast tego dodaj użytkownika do listy kontaktów i wyślij wiadomość w zwyczajny sposób."
		gatewaytranslator = u"Podaj numer ICQ (UIN) użytkownika."

	class cs: # Czech - Mešík (pihhan@cipis.net)
		sessiongreeting = u"Toto je experimentální brána PyICQ-t. Pokud máš problémy prosím kontaktuj Daniela Henningera <jadestorm@nc.rr.com>"
		registertext = u"Prosím zadej tvoje ICQ číslo do kolonky username a heslo do kolonky password."
		notloggedin = u"Chyba. Musíš se před odesíláním zpráv nejprve přihlásit."
		notregistered = u"Promiň. Zdá se že nejsi zaregistrován(a) na této službě. Prosím zaregistruj se a zkus znovu. Pokud máš problémy s registrací, kontaktuj prosím tvého správce Jabberu."
		waitforlogin = u"Promiň, tato zpráva nemůže být ještě doručena. Prosím zkus to znovu až služba dokončí přihlašování."
		groupchatinvite = u"Byl(a) jsi pozván(a) do místnosti ve službě ICQ. Musíš se připojit do místnosti, aby ses přepnul(a) do módu rozhovoru %s.\\nPokud se nepřipojíš, nebudeš se moci zůčastnit rozhovoru, ale stále budeš vypadat jako že jsi se připojil(a) pro kontakty ve službě ICQ."
		groupchatfailjoin1 = u"Nepřipojil(a) ses do místnosti %s.\\nNásledující uživatelé byli v místnosti:"
		groupchatfailjoin2 = u"Byl(a) jsi vyjmut(a) z místnosti ve službě ICQ. Následující bylo řečeno než jsi byl(a) odpojena, když se uživatelům ICQ zdálo že jsi připojena v rozhovoru."
		groupchatprivateerror = u"Promiň. Nemůžeš poslad soukromé zprávy uživatelům v tomto rozhovoru. Namísto toho přidej uživatele do kontaktů a piš jim tou cestou."
		gatewaytranslator = u"Zadej uživatelovo ICQ číslo."

	class nl: # Dutch - Matthias therry (matthias.therry@pi.be)
		sessiongreeting = u"Dit is het experimentele transport, PyICQ-t. In geval van problemen, contacteer dan Daniel Henninger <jadestorm@nc.rr.com>"
		registertext = u"Voer je ICQ-nummer en je wachtwoord in."
		notloggedin = u"Fout: Je moet eerst aanmelden op het transport alvorens berichten te versturen."
		notregistered = u"Sorry, je bent niet geregistreerd op dit transport. Registreer je eerst en probeer dan opnieuw. Contacteer de beheerder van je Jabberserver bij registratieproblemen."
		waitforlogin = u"Sorry, dit bericht kon nog niet worden afgeleverd. Probeer opnieuw wanneer het transport klaar is met aanmelden."
		groupchatinvite = u"Je bent uitgenodigd voor een groepsgesprek op het ICQ-netwerk. Neem deel door om te schakelen naar groepsgesprekmodus %s.\\nAls je dit niet doet zal je niet kunnen deelnemen aan het gesprek, hoewel het voor de ICQ-gebruikers lijkt alsof je toch aanwezig bent."
		groupchatfailjoin1 = u"Je hebt niet deelgenomen aan het groepsgesprek %s.\\nVolgende gebruikers zaten in het gesprek:"
		groupchatfailjoin2 = u"Je bent verwijderd uit het groepsgesprek op het ICQ-netwerk. Het volgende werd gezegd voor de verbinding werd verbroken, terwijl je voor de andere deelnemers van het groepsgesprek aanwezig leek."
		groupchatprivateerror = u"Sorry, je kan geen privé-berichten sturen naar gebruikers in dit groepsgesprek. Voeg ze toe aan uw contactlijst om hen privé te kunnen spreken."
		gatewaytranslator = u"Voer het ICQ-nummer van de gebruiker in."
	nl_NL = nl
	dut = nl
	nla = nl

	class ru: # Russian - Sergey Kirienko (abonentu@pisem.net)
		sessiongreeting = u"Это экспериментальный шлюз PyICQ-t. Если у вас возникли вопросы, пожалуйста, свяжитесь с Дэниэлом Хеннигером (Daniel Henninger) <jadestorm@nc.rr.com>"
		registertext = u"Введите ваш номер ICQ и пароль."

		notloggedin = u"Ошибка. Вы должны зарегистрироваться в службе, перед тем как отправлять сообщения."
		notregistered = u"Извините. Вы не зарегистрированы в этой службе. Зарегистрирутесь и попробуйте снова. В крайнем случае обратитесь к администратору вашего сервера Jabber."
		waitforlogin = u"Сообщение пока не может быть доставлено. Подождите, пока служба выполнит регистрацию."
		groupchatinvite = u"Вы приглашены в комнату бесед. Чтобы участвовать в групповой беседе %s, вам нужно принять приглашение.\\nЕсли вы не присоединитесь, вы не сможете участвовать в групповой беседе, но все равно будете видны как участник беседы."
		groupchatfailjoin1 = u"Вы не присоединились к комнате бесед %s.\\nВ комнате были пользователи:"
		groupchatfailjoin2 = u"Вы вышли из комнаты бесед. Следующее было сказано перед вашим выходом из комнаты."
		groupchatprivateerror = u"Извините. Вы не можете посылать личные сообщения в групповой беседе. Добавьте пользователя в ваш список и и после этого отправьте ему сообщение."
		gatewaytranslator = u"Введите номер ICQ пользователя."