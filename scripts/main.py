import requests
import time
from bs4 import BeautifulSoup
import fileinput
import json
import concurrent.futures
biglist = []

url = [
    'https://google.qwiklabs.com/public_profiles/4bb47dc4-285d-44a3-b59c-ed28eaa02f15', 'https://www.qwiklabs.com/public_profiles/ad0d0752-2fcd-4fd2-a825-96f67b5a3eb8','https://google.qwiklabs.com/public_profiles/b7f6b316-3f98-419e-a37a-b97f0f125d81','http://www.qwiklabs.com/public_profiles/611b45c0-87e3-4456-a09b-2b566b588570', 'https://www.qwiklabs.com/public_profiles/dd65588d-ca95-4b0c-87b6-3dfa33dd712', 'https://google.qwiklabs.com/public_profiles/f98d0f2d-7f67-414b-be3b-32fc8835f060', 'https://google.qwiklabs.com/public_profiles/3cc3582f-e73c-40d7-a1be-a7f499e8b6d9', 'https://www.qwiklabs.com/public_profiles/cbe4183d-7427-46fa-b377-16b84bad367c', 'https://google.qwiklabs.com/public_profiles/668110b2-12cd-49c3-8e3d-3f45b6492176', 'https://google.qwiklabs.com/public_profiles/0bf7bbbf-20c4-47d7-8595-5fe99f6205e2', 'https://www.qwiklabs.com/public_profiles/8302945c-5357-4309-9704-27f62ae27253', 'https://google.qwiklabs.com/public_profiles/cd7a266a-a18a-4343-8f25-d6548310b5dc', 'https://google.qwiklabs.com/public_profiles/d9d01fc9-5841-492a-af7a-704e52a8b3a4', 'https://google.qwiklabs.com/public_profiles/b2a7385c-cd44-4594-b426-533e8ac6bac4', 'https://google.qwiklabs.com/public_profiles/6eddd945-fe4a-485a-bb33-d50c84f9ba63', 'https://google.qwiklabs.com/public_profiles/5121195c-85e5-42b1-a196-f320a18e68f6', 'https://google.qwiklabs.com/public_profiles/80dbd63a-66b4-43b0-aa21-6d5ce7d88dc5', 'https://www.qwiklabs.com/public_profiles/c7a34254-1799-4740-9267-ec307b72ce15', 'https://www.qwiklabs.com/public_profiles/dc662fa0-3e6d-44ec-85f2-07dd0b95012c', 'https://google.qwiklabs.com/public_profiles/a61fbe72-020c-4ba1-9fa0-b845079598b4', 'https://google.qwiklabs.com/public_profiles/a88f221c-c0b3-4ee6-8ff5-bc9c1a2106a9', 'https://www.qwiklabs.com/public_profiles/18bae420-1f0c-4bd6-bd7e-355370039d15', 'https://www.qwiklabs.com/public_profiles/2a57d96e-0b5c-483d-ade5-6099836e43c2', 'https://google.qwiklabs.com/public_profiles/3f50ee16-9365-4a68-8ec6-aaa8230e457a', 'https://www.qwiklabs.com/public_profiles/e7f22520-6791-429a-8341-9a5bc8f34f5c', 'https://google.qwiklabs.com/public_profiles/7d0e0821-abd1-4fe4-a966-01d6e7aa1389', 'https://google.qwiklabs.com/public_profiles/c8ee4598-19ef-4fa6-8b64-1847a137bed2', 'https://www.qwiklabs.com/public_profiles/82f54a3c-f371-4b83-bf9a-6f2ba162b88e', 'https://google.qwiklabs.com/public_profiles/34ae3e92-b617-44c9-8067-e3500eeb7e59', 'https://www.qwiklabs.com/public_profiles/bfb37499-2ae3-438b-864e-36097b7d277f', 'https://google.qwiklabs.com/public_profiles/a568b0d2-453a-4fa8-8f59-34ad4951d38e', 'https://www.qwiklabs.com/public_profiles/e7e06ff0-7b08-48ae-9a9e-b4a9e83c62d6', 'https://google.qwiklabs.com/public_profiles/45838886-2273-4995-bc89-45c14251b389', 'https://www.qwiklabs.com/public_profiles/d3d12710-edbe-495f-85c6-d9cc16baed60', 'https://www.qwiklabs.com/public_profiles/1df6c5f1-b8b1-464b-8cbb-bdd100e72edf', 'https://google.qwiklabs.com/public_profiles/bd30c839-6de4-4e9a-90fb-5589c2a1b354', 'https://google.qwiklabs.com/public_profiles/c0a3d3b7-45a4-481c-9b8f-d256c8f96b44', 'https://google.qwiklabs.com/public_profiles/7d8c43ef-6268-41c6-80bc-7172368402ab', 'https://www.qwiklabs.com/public_profiles/e23e5e54-98bf-4096-b06f-ba964094687e', 'https://google.qwiklabs.com/public_profiles/d84c1c6e-21a4-4baf-9089-d58490ac77ae', 'https://google.qwiklabs.com/public_profiles/371bb668-67d4-4ffb-82a4-ec40d6d92868', 'https://google.qwiklabs.com/public_profiles/c664c7dd-1b40-441e-9679-0e651bcec853', 'https://www.qwiklabs.com/public_profiles/a40c8e6d-81dd-4247-9e2f-0112fc1ed529', 'https://www.qwiklabs.com/public_profiles/ecb0b75c-fdcc-4ac1-8020-fe8e98753e78', 'https://google.qwiklabs.com/public_profiles/6a889933-ed8f-43d8-bbfb-fdbf75d31ce1', 'https://google.qwiklabs.com/public_profiles/e04f1d2a-fbc0-4704-a0f2-f9e80fe3dfce', 'https://google.qwiklabs.com/public_profiles/6da8783c-7656-4700-a92d-235f9466a355', 'https://google.qwiklabs.com/public_profiles/1e26f655-7d89-4c2f-936a-43ed04bda69b', 'https://www.qwiklabs.com/public_profiles/d55a09f7-7de7-47fd-8040-f6f3751cac68', 'https://google.qwiklabs.com/public_profiles/afdbc6b1-18bc-471e-b2e1-317bc06dc079', 'https://google.qwiklabs.com/public_profiles/315fcd0c-49ee-4387-9735-fd0b3677754f', 'https://google.qwiklabs.com/public_profiles/3b5442a1-b18b-44d0-897e-89ff33f422d7', 'https://google.qwiklabs.com/public_profiles/bac549cb-9881-4f6e-abe3-f335c0ca7c98', 'https://www.qwiklabs.com/public_profiles/e3f0ce7e-760b-42b2-8547-83fdac7a846d', 'https://google.qwiklabs.com/public_profiles/18f7b56b-3978-4f62-896d-0a60036039dc', 'https://www.qwiklabs.com/public_profiles/7a737b65-dbfc-45ff-b9bb-685542e9b2d7', 'https://www.qwiklabs.com/public_profiles/f8527fd4-9b66-4a87-8b85-1cf5fb753a5a', 'https://google.qwiklabs.com/public_profiles/d1e58e89-8eb3-4185-a91e-d8ea75806ad0', 'https://www.qwiklabs.com/public_profiles/13328a6e-b4a2-4747-a4f3-5bd3fb1e7bae', 'https://run.qwiklabs.com/public_profiles/58066fcf-0cd4-4910-97ae-9069ff64614b', 'https://www.qwiklabs.com/public_profiles/64caf2b4-91b6-4c4a-a740-8765fb3fdb87', 'https://google.qwiklabs.com/public_profiles/5dd8df98-f7d2-46b0-9ae0-beb568a82595', 'https://google.qwiklabs.com/public_profiles/8784e522-8670-45c0-a5cf-d1d7afcd611d', 'https://google.qwiklabs.com/public_profiles/0f72500a-9945-4bba-8254-456fda30f7b9', 'https://google.qwiklabs.com/public_profiles/1aa3bd77-510f-47cb-93ff-063f24988c73', 'https://www.qwiklabs.com/public_profiles/de8a6504-400c-49dc-8fc2-070d65b942df', 'https://google.qwiklabs.com/public_profiles/b0bad55c-3087-4e7f-a3bc-84e8a1633ac8', 'https://www.qwiklabs.com/public_profiles/8666f292-7c40-4975-a29b-75e866e8479c', 'https://google.qwiklabs.com/public_profiles/da7289c0-6eb8-45b8-a2b4-2c6c37a32700', 'https://google.qwiklabs.com/public_profiles/1715f489-f6a9-413a-9da5-18598029acc8', 'https://google.qwiklabs.com/public_profiles/008cce31-c345-4197-9961-9fd313ad9676', 'https://www.qwiklabs.com/public_profiles/12c363b7-c4c2-42f7-98f0-aa0339b77b18', 'https://google.qwiklabs.com/public_profiles/663e0478-12b2-4926-921f-5709fa226bce', 'https://google.qwiklabs.com/public_profiles/095e071a-de52-4429-b94a-5c1c80e22231', 'https://www.qwiklabs.com/public_profiles/4040ddd0-b4c4-49f9-8762-a206d01a6cca', 'https://run.qwiklabs.com/public_profiles/306ea662-d183-424d-99cb-53d4c0fc917f', 'https://google.qwiklabs.com/public_profiles/787d9ed9-fdd1-4da7-bcd9-082270252adf', 'https://google.qwiklabs.com/public_profiles/a9b6311e-2d9a-42f5-90e0-f64d96402edb', 'https://www.qwiklabs.com/public_profiles/608c8380-179b-4d25-9e84-79d25ad4554e', 'https://www.qwiklabs.com/public_profiles/a5467062-b26e-4eb8-9480-200bf97871d1', 'https://google.qwiklabs.com/public_profiles/fde8062a-1ff6-4423-9c8c-486127fc9cb1', 'https://google.qwiklabs.com/public_profiles/421ec7e0-82b7-4571-81f5-9903b5971903', 'https://google.qwiklabs.com/public_profiles/05f78855-b622-4744-9050-a917fe3141ef', 'https://google.qwiklabs.com/public_profiles/604cde3d-ebbd-4fab-9a61-0a82cd67a08c', 'https://www.qwiklabs.com/public_profiles/dcc42971-1c0b-4e04-b8cd-4075d0afdf5b', 'https://www.qwiklabs.com/public_profiles/1c7a7154-fafd-421e-84f1-17f42769106f', 'https://google.qwiklabs.com/public_profiles/bc44d640-17a8-47b2-b7f2-fa360a02eed6', 'https://www.qwiklabs.com/public_profiles/f30a2adb-e413-451a-9afa-5d539243fef5', 'https://google.qwiklabs.com/public_profiles/0f6b423c-c20c-42c7-b526-1d6440724e26', 'https://www.qwiklabs.com/public_profiles/ed93fa9a-734e-4919-ab9f-9b099deb407f', 'https://google.qwiklabs.com/public_profiles/caa878fe-5ac3-4f7d-bbc8-5d677c809aa1', 'https://google.qwiklabs.com/public_profiles/06f4d4cf-08c0-418c-a3e8-38b63de419ca', 'https://www.qwiklabs.com/public_profiles/6a68cd6b-f782-4218-9b9b-fae89c0c77c0', 'https://google.qwiklabs.com/public_profiles/b49dac4f-eed6-46c7-b9dc-c8ee3db6e8fa', 'https://google.qwiklabs.com/public_profiles/8173e6e7-bae1-43cb-84fa-1e8ecbffbd31', 'https://google.qwiklabs.com/public_profiles/1e33fb94-446a-4187-a8cd-6afcfad7ece2', 'https://google.qwiklabs.com/public_profiles/1c20ccb6-7be2-4099-83c1-5adad3378885', 'https://www.qwiklabs.com/public_profiles/337cde44-4da5-48f1-a3ee-57f8148a5062', 'https://google-run.qwiklabs.com/public_profiles/91991d68-f942-4c81-861b-80e967c45ab1', 'https://google.qwiklabs.com/public_profiles/2430e548-ce90-40ca-8694-9e0c10045b80', 'https://www.qwiklabs.com/public_profiles/532b0e9f-fbd0-488f-84cf-7209c54383ad', 'https://google.qwiklabs.com/public_profiles/043e3cfa-c578-4f97-a0c0-b4728783a89e', 'https://google.qwiklabs.com/public_profiles/1455ca4a-f7bf-4e67-942e-8e5d722e4dcc', 'https://www.qwiklabs.com/public_profiles/643f7a9f-dd04-47b7-8bbc-c3cd3f045db1', 'https://google.qwiklabs.com/public_profiles/b0f90dcd-3a6d-4457-96c7-3eea918dead8', 'https://www.qwiklabs.com/public_profiles/d4d8f237-1d5e-4dc3-a24f-0d22a0c8b623', 'https://run.qwiklabs.com/public_profiles/3c91676f-9e84-450b-8cbb-89705a272f80', 'https://google.qwiklabs.com/public_profiles/4bbe3b63-647c-4392-98d6-2f17ede0793f', 'https://google.qwiklabs.com/public_profiles/83f82de6-b846-4e8a-8fd2-f4d9f6dbdf22', 'https://google.qwiklabs.com/public_profiles/90e4186a-e27e-4228-8fec-82fd5a5e7f65', 'https://google.qwiklabs.com/public_profiles/6b615594-2184-4b60-9b3c-bef5ca577e97', 'https://run.qwiklabs.com/public_profiles/81f6b62b-6fc4-4e26-ac14-a4e6cc76781d', 'https://google.qwiklabs.com/public_profiles/6f2514a9-bdad-467f-a267-c592de59dfbb', 'https://www.qwiklabs.com/public_profiles/ca596328-c572-4d46-a17b-2ea34e199d41', 'https://google.qwiklabs.com/public_profiles/60e9a545-0ad0-49a4-91fe-cf4b88b7efb4#', 'https://www.qwiklabs.com/public_profiles/5f8a46ae-7a29-4af2-87e6-f5fc93e2d397', 'https://google.qwiklabs.com/public_profiles/f3540ed7-71d3-4338-91e9-4200f511300f', 'https://google.qwiklabs.com/public_profiles/29cc66fc-154f-4e52-8e8a-d4c5b0717c87', 'https://google.qwiklabs.com/public_profiles/e79f31e9-e320-4073-8a42-1ef07b5e9423', 'https://www.qwiklabs.com/public_profiles/0691fcf4-ab47-400c-a878-dd959f582a38', 'https://google.qwiklabs.com/public_profiles/fe99205a-92de-4b52-bd9f-102d34840cd3', 'https://www.qwiklabs.com/public_profiles/08b81b5c-8854-4509-aa5b-c3a2254cd2d4', 'https://google-run.qwiklabs.com/public_profiles/f4fd8fdc-c0b2-413d-8842-c37e2a369cdf', 'https://www.qwiklabs.com/public_profiles/48e535e7-9f1e-4f0a-a87e-4cb7e3390ba7', 'https://google.qwiklabs.com/public_profiles/9651d371-15b8-46b3-9e5a-3bf75d325f32', 'https://www.qwiklabs.com/public_profiles/b5f94756-0a57-4d0d-bf03-f7ab80aefbbe', 'https://google.qwiklabs.com/public_profiles/460d3aef-2103-4869-b9a1-ba100a7df9f8', 'https://google.qwiklabs.com/public_profiles/f588a367-5275-4d5f-9d51-eb079ece90ee', 'https://google.qwiklabs.com/public_profiles/55d00de0-21ee-45a4-94cb-f81da198991b', 'https://www.qwiklabs.com/public_profiles/c0ee8ccf-3cc1-45aa-bea5-811b9a8ae667', 'https://google.qwiklabs.com/public_profiles/9d6844a3-4d83-4e27-83fc-7d41346a5524', 'https://google.qwiklabs.com/public_profiles/3f8500d1-35b4-4536-96ab-a21350e76857', 'https://google.qwiklabs.com/public_profiles/8f7cf8f1-7625-4ebb-875c-5c942832a945', 'https://google.qwiklabs.com/public_profiles/e6b16639-802a-406b-ba96-ffddaa61660f', 'https://google.qwiklabs.com/public_profiles/fac9e5b9-eead-4596-b01c-5fffaa58cc98', 'https://google.qwiklabs.com/public_profiles/ea06c197-cc5e-4b6a-8bd8-2b70fa3fa9f0', 'https://www.qwiklabs.com/public_profiles/5174cfb6-e583-4c7e-9895-55e9abae5fa0', 'https://google.qwiklabs.com/public_profiles/3205efc1-4d39-45f6-9c46-cf58d674e27b', 'https://www.qwiklabs.com/public_profiles/f6987f8e-c658-4dcf-9cef-32dbfdb5a544', 'https://www.qwiklabs.com/public_profiles/0c61a49f-a17e-46f2-a5c2-27e24af63bf5', 'https://google.qwiklabs.com/public_profiles/e8168730-74e7-49e2-b2a1-187e364f54db', 'https://google.qwiklabs.com/public_profiles/6bc7e0be-eb5b-454e-970b-452579319854', 'https://www.qwiklabs.com/public_profiles/332f3473-d093-4c53-af47-a4653261e0b6', 'https://google-run.qwiklabs.com/public_profiles/8ba130c9-bbfa-445a-bb20-0e218f60fa18', 'https://google.qwiklabs.com/public_profiles/61e24784-f35b-4290-bc74-4321a91f63a7', 'https://google-run.qwiklabs.com/public_profiles/9d7160a9-fb65-47ea-9a9d-d35ccb40154e', 'https://www.qwiklabs.com/public_profiles/2a8893f4-44b4-4fdf-97ac-6dbd758e8702', 'https://www.qwiklabs.com/public_profiles/d792659b-dbff-42aa-b38e-785e349a084a', 'https://google.qwiklabs.com/public_profiles/207013df-79d1-4532-a82e-dbdac8298bc3', 'https://google.qwiklabs.com/public_profiles/5788334a-19cb-435d-9f4c-16ea7c1b753f', 'https://google.qwiklabs.com/public_profiles/85d093fa-620a-46e0-9968-7422fad5a4c0', 'https://www.qwiklabs.com/public_profiles/39037f66-ddbd-421a-916b-7061e0e9dea4', 'https://google.qwiklabs.com/public_profiles/39e9b2e7-afca-4af1-9c18-17a4676ce97c', 'https://google.qwiklabs.com/public_profiles/9f566a6e-4a48-4744-a22b-ce0541d97726', 'https://google.qwiklabs.com/public_profiles/a580d9b0-a364-403f-ad49-6eeae6c641b4', 'https://google.qwiklabs.com/public_profiles/d9288e18-52ce-4d54-aacc-244bd713589d', 'https://google.qwiklabs.com/public_profiles/9997376b-a12d-4022-aff5-dfaa8dedfa09', 'https://google.qwiklabs.com/public_profiles/7f5a870e-1101-4397-8cf9-bd9f3e499071', 'https://google.qwiklabs.com/public_profiles/32c5f736-8dff-4ace-af29-7483f1e9fab3', 'https://google.qwiklabs.com/public_profiles/fa2fe9f7-6dff-4c53-abf7-43fb76fffb70', 'https://www.qwiklabs.com/public_profiles/025069ac-45c2-400c-afa3-abe08eab2036', 'https://google.qwiklabs.com/public_profiles/bda19b65-8c8f-45b5-8e78-5bb5a67548ae', 'https://google.qwiklabs.com/public_profiles/972c8151-f264-4aa3-8088-86e0ef9e9813', 'https://google.qwiklabs.com/public_profiles/5d985e47-2b72-490d-a530-4edfab810f79', 'https://google.qwiklabs.com/public_profiles/7a1f284d-6d8c-4c5c-b86a-ea2ef08a8189', 'https://google.qwiklabs.com/public_profiles/30ceba83-af3c-4526-bd52-2ea27a34ab79', 'https://www.qwiklabs.com/public_profiles/baca0956-7f84-48cd-9e98-ea85534df7d7', 'https://google.qwiklabs.com/public_profiles/667c2380-4800-4a5c-95bc-0c601723ef6b', 'https://google.qwiklabs.com/public_profiles/134de938-5fc2-4c92-989e-05a7de43edab', 'https://www.qwiklabs.com/public_profiles/65d0cf8b-719b-4256-80ea-83942a343dce', 'https://google.qwiklabs.com/public_profiles/9958b309-fb7f-4bbb-a2db-3dd83ac9f7b6', 'https://www.qwiklabs.com/public_profiles/36aa7172-1a00-4d74-9871-6b2f6552a00b', 'https://www.qwiklabs.com/public_profiles/c64420e3-83cf-4b19-bf51-071720fd7f3e', 'https://google.qwiklabs.com/public_profiles/4172edde-c0e9-4c42-b404-ec5c14acd110', 'https://www.qwiklabs.com/public_profiles/8ac419ac-7694-4ca5-819e-258dd350d02f', 'https://www.qwiklabs.com/public_profiles/d28c8e63-fefd-4b59-87a6-8e3a4b092dc5', 'https://www.qwiklabs.com/public_profiles/06f6d3b7-7557-4cd4-9cb0-b811ea565fc0', 'https://www.qwiklabs.com/public_profiles/cc7172eb-8377-42d4-ad97-cfda77cf3ab2', 'https://www.qwiklabs.com/public_profiles/e4c0a11d-b6c3-4810-9171-4ad7835f8c4d', 'https://www.qwiklabs.com/public_profiles/9dab22f0-1bf8-412a-afe7-2a629e493b58', 'https://www.qwiklabs.com/public_profiles/25bb3e6a-5364-4e6b-a2e5-885f71d397c8', 'https://google.qwiklabs.com/public_profiles/231200b5-40de-43b4-b3ad-9445ce0e99bf', 'https://google.qwiklabs.com/public_profiles/c5e83619-eb36-4556-aa36-71b4a8d8c8f7'
]


track1 = [
    'Getting Started: Create and Manage Cloud Resources',
    'Perform Foundational Infrastructure Tasks in Google Cloud',
    'Set up and Configure a Cloud Environment in Google Cloud',
    'Deploy and Manage Cloud Environments with Google Cloud',
    'Build and Secure Networks in Google Cloud',
    'Deploy to Kubernetes in Google Cloud'
]
track2 = [
    'Getting Started: Create and Manage Cloud Resources',
    'Perform Foundational Data, ML, and AI Tasks in Google Cloud',
    'Insights from Data with BigQuery',
    'Engineer Data in Google Cloud',
    'Integrate with Machine Learning APIs',
    'Explore Machine Learning Models with Explainable AI'
]


def data_scraping(url):
    start_thread(url)


def data_gathering(link):
    tempdic = {}
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    track1completed = []
    track2completed = []
    profile = soup.findAll('div', attrs={'class': 'public-profile__hero'})[0]
    dp = profile.img['src']
    name = profile.h1.text
    tempdic['name'] = name.strip()
    tempdic['dp'] = dp
    quests = soup.findAll('ql-badge')
    for quest in quests:
        allquest = json.loads(quest.get('badge'))['title']
        if allquest in track1:
            track1completed.append(allquest)
        if allquest in track2:
            track2completed.append(allquest)
    tempdic['track1'] = track1completed
    tempdic['track2'] = track2completed
    tempdic['qcomplete_no'] = len(track1completed) + len(track2completed)
    if tempdic['qcomplete_no'] != 0:
        #print(len(biglist)," ",tempdic['name']," ",tempdic['qcomplete_no']," ",tempdic['track1']," ",tempdic['track2'])
        biglist.append(tempdic)
        print("data saved")
    else:
        print("no badges")


def data_saving(biglist):
    res = sorted(biglist, key=lambda x: x['qcomplete_no'], reverse=True)
    with open("my.json", "w") as f:
        json.dump(res, f)
    f.close()
    print(len(res), "started doing labs")
    # print(res)


def start_thread(url2):
    threads = 30
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(data_gathering, url2)
    data_saving(biglist)


def main(url):
    data_scraping(url)


if __name__ == '__main__':
    #t0 = time.time()
    main(url)
    #t1 = time.time()
    #print(f"{t1-t0} seconds to download {len(url2)} profile.")
    #print("number of people started",len(biglist))
