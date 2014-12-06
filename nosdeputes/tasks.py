# -*- coding: utf-8 -*-




def download_liasse_order(id_loi, id_dossier, id_examen):
    url = "http://www2.assemblee-nationale.fr/recherche/query_amendements?typeDocument=amendement&idExamen=%s&idDossierLegislatif=%s&numAmend=&idAuteur=&idArticle=&idAlinea=&sort=&dateDebut=&dateFin=&periodeParlementaire=&texteRecherche=&rows=2500&format=html&tri=ordreTexteasc&typeRes=liste&start=" % (id_examen, id_dossier)