#!/bin/bash
echo -e "\e[32m[IA_ZERO.07] Moteur Shell Actif (VULN-204427_VERIFIED)\e[0m"
# Logique de filtrage rapide
anonymize() { sed -E 's/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/[EMAIL_HIDDEN]/g'; }
echo "Test : admin@milyes.io" | anonymize
