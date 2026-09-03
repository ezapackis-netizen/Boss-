from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

print("JARVIS ir gatavs.")
print("Raksti komandu. Lai izietu, raksti: exit")

while True:
    user = input("\nTu: ")

    if user.lower() in ["exit", "quit", "stop"]:
        print("JARVIS: Uz redzēšanos.")
        break

    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions="""
Tu esi JARVIS tipa personīgais asistents.
Atbildi latviski, īsi un saprotami.
Esi gudrs, mierīgs un praktisks.
Lietotāju sauc Elviss.
Ja lietotājs dod komandu, paskaidro, ko vari izdarīt.
Nekad neizliecies, ka esi izdarījis darbību, ja tā nav faktiski izpildīta.
""",
        input=user
    )

    print("JARVIS:", response.output_text)
