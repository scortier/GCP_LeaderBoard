import requests
import time
from bs4 import BeautifulSoup
import fileinput
import json
import concurrent.futures
biglist=[]
smalllist=[]


url =['https://google.qwiklabs.com/public_profiles/084c2e19-f7a8-4319-a840-5e3c7905bb25', 'https://google.qwiklabs.com/public_profiles/ac254c96-2f3e-4ec2-995e-30d3ee4eb447', 'https://google.qwiklabs.com/public_profiles/17e137d2-915c-4232-aaeb-9b1970195ccb', 'https://google.qwiklabs.com/public_profiles/98a88b4f-3e4f-409d-b6d4-a70955a00d8d', 'https://google.qwiklabs.com/public_profiles/737622c5-b009-4c44-b543-f90d5ee6af64', 'https://google.qwiklabs.com/public_profiles/d8cb0c3a-075e-4828-a8de-8e3eddd34f44', 'https://google.qwiklabs.com/public_profiles/6a983ad5-dab2-4db4-986e-de4c7bd85cd4', 'https://www.qwiklabs.com/public_profiles/c27cc8a1-2b31-4d8f-97e9-7984b2a36d29', 'https://google.qwiklabs.com/public_profiles/43f6d7a5-350f-497b-937b-df3371502f1d', 'https://www.qwiklabs.com/public_profiles/823faa8a-00d1-4389-b069-814c89201105', 'https://www.qwiklabs.com/public_profiles/7a46353f-15e5-4cba-9946-23b42d0a42db', 'https://google.qwiklabs.com/public_profiles/0eb1f5f5-accb-41d0-a945-0dbb512dfa08', 'https://google.qwiklabs.com/public_profiles/d95ef0e7-ba0d-48f3-8389-abf21432fb02', 'https://google.qwiklabs.com/public_profiles/6ab3a6c9-42a8-415d-a030-93155d82b66e', 'https://google.qwiklabs.com/public_profiles/840c96af-8acb-4a9c-8af9-6c64bd912af2', 'https://google.qwiklabs.com/public_profiles/dde9fcd1-a669-4972-bf97-8e35b448a1fb', 'https://google.qwiklabs.com/public_profiles/5b4e62d2-ce6c-4f65-9033-126a3054e1f6', 'https://www.qwiklabs.com/public_profiles/0e21ec94-5cac-4d87-94d7-90b06a709a38', 'https://google.qwiklabs.com/public_profiles/23b49671-55f8-4e39-aec0-f9e0641480f0', 'https://google.qwiklabs.com/public_profiles/4d1ce2b8-1217-4574-872b-320c084b3721', 'https://google.qwiklabs.com/public_profiles/7c7ae3fb-76f7-45e3-9e5b-5619db6a7c89', 'https://www.qwiklabs.com/public_profiles/b699681d-3e30-4433-b579-5ea8972d8164', 'https://google.qwiklabs.com/public_profiles/7828d498-07ab-41c8-bf72-e7c4ee824138', 'https://google.qwiklabs.com/public_profiles/b58d6839-2baa-486a-a922-39834ec19720', 'https://www.qwiklabs.com/public_profiles/380db474-a817-4720-8d34-54da83d37d71', 'https://google.qwiklabs.com/public_profiles/b61f3e19-728f-4c0a-adf8-685b3044cf78', 'https://google.qwiklabs.com/public_profiles/739624df-7c5f-4a58-a563-ddff731cb998', 'https://www.qwiklabs.com/public_profiles/3a1e5fde-359d-4e5d-bd34-1dfdccb002b5', 'https://google.qwiklabs.com/public_profiles/9ff91d0d-f1a9-4f63-bf5d-123e43893cc8', 'https://google.qwiklabs.com/public_profiles/0166f5ba-3767-4925-91b9-80d46930b8f8', 'https://google.qwiklabs.com/public_profiles/cd42b3f6-da9b-40ae-95af-aaa96023ad01', 'https://google.qwiklabs.com/public_profiles/2978e9d5-c6eb-489b-bf6f-511eed47426d', 'https://google-run.qwiklabs.com/public_profiles/c729a89f-acbd-4aff-940d-2a484aea51ab', 'https://www.qwiklabs.com/public_profiles/847aabbf-a39b-4288-bd8b-b3f6e61cbaf7', 'https://google.qwiklabs.com/public_profiles/44836bab-f428-44a3-ab67-65164cfe9bee', 'https://google.qwiklabs.com/public_profiles/d5aa12ba-f5a3-4649-be7e-c0443fff7dc2', 'https://www.qwiklabs.com/public_profiles/563e3146-1a3e-4e63-ae1d-a2daa32e8657', 'https://google.qwiklabs.com/public_profiles/d1e4e366-5eb9-4c6e-967e-71e12edbff37', 'https://www.qwiklabs.com/public_profiles/af3058ef-e3de-4c53-b3cb-cbe843fc9873', 'https://www.qwiklabs.com/public_profiles/b7ccd740-a050-4eb3-884d-711ab1523b04', 'https://www.qwiklabs.com/public_profiles/b7413437-1db4-460c-ad70-5f8a7fdda543', 'https://www.qwiklabs.com/public_profiles/4d5754f6-3ab2-461f-985c-2f995fc0b234', 'https://www.qwiklabs.com/public_profiles/bb1dc92c-ceb1-493b-9955-b9400d60f933', 'https://run.qwiklabs.com/public_profiles/ac2ce5ec-570b-496c-a6cf-f895b56fc509', 'https://www.qwiklabs.com/public_profiles/c7f586aa-652a-4655-8a8f-1d64d4dad2cc', 'https://www.qwiklabs.com/public_profiles/11fae5f1-0559-44c0-8c39-3f9b2ee91d4b', 'https://google.qwiklabs.com/public_profiles/c60ff7db-4a61-4664-82e2-fb9b75a48b7c', 'https://www.qwiklabs.com/public_profiles/68cb0272-8eb1-4d2e-95de-60b0e3bfd80f', 'https://google.qwiklabs.com/public_profiles/e561f397-0ce0-48cc-9267-9ba6db47a4fb', 'https://www.qwiklabs.com/public_profiles/f429a0aa-0ee9-4eb7-b0f9-f0849186f2d1', 'https://google.qwiklabs.com/public_profiles/2a2ed61f-219b-4272-bcdc-3af634dc7104', 'https://google.qwiklabs.com/public_profiles/1f23bd14-c353-478c-abc7-b8643e9f2f2b', 'https://google-run.qwiklabs.com/public_profiles/5e63b92c-6e29-4e7a-ba71-08da4aa4b1b5', 'https://www.qwiklabs.com/public_profiles/84b30026-e620-4dcb-898e-f72eeeb14068', 'https://google.qwiklabs.com/public_profiles/c6b78f92-1c9f-4150-881a-a32ae17ff254', 'https://google.qwiklabs.com/public_profiles/3f7a2170-1f8e-413f-b0c4-4e11356e3a8a', 'https://google-run.qwiklabs.com/public_profiles/d16e869f-6294-4040-adfe-bd7069a24420', 'https://google.qwiklabs.com/public_profiles/0e6d1e96-df7d-444a-b2fb-e89a714595a8', 'https://google.qwiklabs.com/public_profiles/7501a12f-427a-414b-aee0-e1379d6a5f26', 'https://google.qwiklabs.com/public_profiles/0675bf5f-1d1e-4b5e-aac5-7a2f36402055', 'https://www.qwiklabs.com/public_profiles/e0dfef67-a8aa-4e19-bfc2-d733828b7caa', 'https://google.qwiklabs.com/public_profiles/8652d794-4d9c-4ef3-8f7f-7d86bbe99885', 'https://google.qwiklabs.com/public_profiles/36f6c9e8-60f0-4def-8177-95e01e375177', 'https://www.qwiklabs.com/public_profiles/b755dbc5-af2e-4a78-b989-09b708912a26', 'https://google.qwiklabs.com/public_profiles/71edaf73-f546-4404-9511-f8c24a5c212f', 'https://google.qwiklabs.com/public_profiles/d5b83438-a702-4929-8e7c-f77f16499e1a', 'https://google.qwiklabs.com/public_profiles/6363682b-f050-42fa-88cd-c51d64f78b32', 'https://google.qwiklabs.com/public_profiles/8670b7d6-458f-448a-8bdd-148bc448563d', 'https://google.qwiklabs.com/public_profiles/f37b436a-1c32-46cf-8bbd-74df71701f71', 'https://google.qwiklabs.com/public_profiles/7c2d0e5d-cbfa-47a5-9737-a1e171a5a504', 'https://google.qwiklabs.com/public_profiles/65920f1e-1359-4147-b633-9485ba91bbf2', 'https://google.qwiklabs.com/public_profiles/3a259bf0-9c29-4115-ab6e-833491487b14', 'https://google.qwiklabs.com/public_profiles/b1635f8f-d864-4296-963c-49d47c2578fa', 'https://www.qwiklabs.com/public_profiles/f4c1560c-7a61-43c2-81c4-2c3b20cc78c4', 'https://google.qwiklabs.com/public_profiles/59dff8df-ef63-4453-b905-b57613fbfa7c', 'https://google.qwiklabs.com/public_profiles/f3848e28-0ce8-4a28-9a55-4dbd2263ce8e', 'https://google.qwiklabs.com/public_profiles/c42a3ce7-cd13-484e-80c6-6d09235f3ae8', 'https://www.qwiklabs.com/public_profiles/d003fd4b-bcc1-40a4-9b9e-e39fbca345a7', 'https://google.qwiklabs.com/public_profiles/d0467fad-27f6-4739-9dc7-bf385b510eb3', 'https://google.qwiklabs.com/public_profiles/ee78d8f8-ac76-4c2e-bc98-dce3004bbf8f', 'https://www.qwiklabs.com/public_profiles/7d814f75-8afc-4442-88ad-d2b32e6772c9', 'https://google.qwiklabs.com/public_profiles/f6e8afda-ea1b-486c-b951-b7025e0fca12', 'https://google.qwiklabs.com/public_profiles/f3d5ccaf-a404-4449-b362-f99a83bb1be0', 'https://www.qwiklabs.com/public_profiles/153a1fe1-c41b-422a-9b2f-bb7ca164f364', 'https://www.qwiklabs.com/public_profiles/1625f428-f914-4896-90cb-4be7d9a30e4c', 'https://www.qwiklabs.com/public_profiles/c8a7127c-d9af-447b-b565-39c7c86feffa', 'https://www.qwiklabs.com/public_profiles/b552d926-90ec-43d4-bb1b-d1e6713c2baa', 'https://google.qwiklabs.com/public_profiles/01dba269-4331-437b-b1fa-5c7907ac071a', 'https://google.qwiklabs.com/public_profiles/77def105-33bb-4005-9cd6-bb20c417029a', 'https://www.qwiklabs.com/public_profiles/38f2950e-e62a-40fb-a88a-930138375961', 'https://google.qwiklabs.com/public_profiles/28387534-c481-47fd-8db7-b3aa09714ae4', 'https://google.qwiklabs.com/public_profiles/d28b585d-f6df-4759-ac32-084064718d01', 'https://www.qwiklabs.com/public_profiles/8d945bdb-b31e-4060-adb1-dfcb2c4e0db3', 'https://www.qwiklabs.com/public_profiles/f73200dc-ea34-4a5e-8525-8bca9735f333', 'https://www.qwiklabs.com/public_profiles/2605dea1-8236-4109-94ea-feb751fdbf39', 'https://google.qwiklabs.com/public_profiles/c20eb093-6947-49b6-a5ee-723629d33ffb', 'https://www.qwiklabs.com/public_profiles/41c7a527-661a-4629-996a-7b828e02f130', 'https://google.qwiklabs.com/public_profiles/85929087-9909-41fc-b638-18416fb4b3e6', 'https://google.qwiklabs.com/public_profiles/49079ef6-f3fb-427d-891f-e2559a205dda', 'https://google.qwiklabs.com/public_profiles/ed27d58b-850d-45ce-8120-c67818b81145', 'https://google.qwiklabs.com/public_profiles/d920937a-6df0-43ee-bc1a-d64a4c86b120', 'https://www.qwiklabs.com/public_profiles/08c2e7c6-79d4-4c21-b2d7-c74bb31501a1', 'https://google.qwiklabs.com/public_profiles/33285675-85b3-4a51-b117-ec77edde6081', 'https://google.qwiklabs.com/public_profiles/0c87a686-e1c5-436f-92f9-3c3a166b997a', 'https://google.qwiklabs.com/public_profiles/15ca84fe-bc0b-4802-a03c-598e514c6a2e', 'https://google.qwiklabs.com/public_profiles/bac2eba4-202a-4024-8411-70bed222d05a', 'https://www.qwiklabs.com/public_profiles/513fee7a-cdd0-4c77-a68a-080643c6c8ae', 'https://www.qwiklabs.com/public_profiles/c7ed8298-6e2c-4b6a-9218-ab1fc3baff75', 'https://google.qwiklabs.com/public_profiles/eef99a53-03db-4bfb-a54b-c459615a93bc', 'https://www.qwiklabs.com/public_profiles/026b4361-eb46-4ffd-a479-025f14ed53d3', 'https://www.qwiklabs.com/public_profiles/d23ea160-09ec-4a19-966c-287f0da420d3', 'https://www.qwiklabs.com/public_profiles/07dec915-7a24-426a-9eee-eee53435850e', 'https://google.qwiklabs.com/public_profiles/e5e4ee2e-8a9e-44f7-9f9e-1338fb583bd7', 'https://google.qwiklabs.com/public_profiles/f6a88f11-1f6e-4431-9a53-ea4be88ecc84', 'https://google.qwiklabs.com/public_profiles/477f879b-79a0-4e24-9d20-d327f7c382d1', 'https://google.qwiklabs.com/public_profiles/20b41646-dcd9-479a-be6d-c6777c6a490e', 'https://google.qwiklabs.com/public_profiles/83b39641-be6e-413c-9d72-2a71cb4437c8', 'https://www.qwiklabs.com/public_profiles/204ac9e6-14db-4f12-9f88-dcf58fe1021d', 'https://google.qwiklabs.com/public_profiles/591e78ff-8310-447a-9db4-1ff0188fe004', 'https://google.qwiklabs.com/public_profiles/278cbf04-7f44-45e7-8691-942ad0a5b382', 'https://google.qwiklabs.com/public_profiles/70e031bc-e82c-405d-98df-cdf7ece30bd1', 'https://google.qwiklabs.com/public_profiles/d4603f20-1b67-41cd-9ca7-3e2a22a59cc1', 'https://www.qwiklabs.com/public_profiles/33abc4e6-2f8f-4422-9126-8445d522bf9b', 'https://google.qwiklabs.com/public_profiles/92350e04-d1cd-47ad-a08e-9de61f129ab6', 'https://google.qwiklabs.com/public_profiles/30664860-f6c2-4e7b-bc47-ade53ad06dda', 'https://www.qwiklabs.com/public_profiles/efba86e5-8078-43a5-9b3b-286bfa9713e3', 'https://google.qwiklabs.com/public_profiles/c487dd85-2719-4fe0-9101-19cf4ee0c294', 'https://www.qwiklabs.com/public_profiles/ad8a1cc6-9d5b-4fbe-9e24-2a6407ef4deb', 'https://google.qwiklabs.com/public_profiles/a3bcbb24-017b-4df3-941a-41f173bd321e', 'https://google.qwiklabs.com/public_profiles/f6fdeb2a-bdfb-41e4-b703-6d6921fae23d', 'https://google.qwiklabs.com/public_profiles/0a0104cd-2b6e-4876-a4c9-9045f580a44a', 'https://google.qwiklabs.com/public_profiles/64935b38-6485-4d54-bcf6-52ecb3d78585', 'https://www.qwiklabs.com/public_profiles/b5b76fa8-f4f5-47a3-b87f-92afb12acf7d', 'https://www.qwiklabs.com/public_profiles/5d22e6ed-19ef-4ee4-8fcd-be889dcfca7c', 'https://google.qwiklabs.com/public_profiles/d2c48ac6-f379-43c3-9ec0-f1a6fdedd2f4', 'https://google.qwiklabs.com/public_profiles/a8458aa5-2483-4443-b4a1-f164aaa49a23', 'https://www.qwiklabs.com/public_profiles/62f45f1b-8a88-4f08-9958-4fe2dd62af0d', 'https://www.qwiklabs.com/public_profiles/c52e188f-200f-41af-8027-3ad8a783841a', 'https://google.qwiklabs.com/public_profiles/2444205f-804f-4392-9833-19c6034ad817', 'https://www.qwiklabs.com/public_profiles/687fa209-744b-4d72-b61c-1d50395fa0bd', 'https://www.qwiklabs.com/public_profiles/35890b49-dc31-4345-a660-fa2818869a7c', 'https://www.qwiklabs.com/public_profiles/654a21a9-2929-42ed-a108-839db183ca82', 'https://google.qwiklabs.com/public_profiles/d05e516e-eccd-4e81-b6bc-1c260a5fc8bf', 'https://www.qwiklabs.com/public_profiles/d93857cd-abe6-46a1-be7d-26a657a5968f', 'https://google.qwiklabs.com/public_profiles/031a8431-fd20-41e4-b69f-10291d9a75db', 'https://google.qwiklabs.com/public_profiles/48477abc-d0e4-4088-b0c4-66f36fa3db1f', 'https://www.qwiklabs.com/public_profiles/5d012573-26a8-4187-9289-f41fca4bc353', 'https://google.qwiklabs.com/public_profiles/1a4f3a50-673b-4e5a-a99b-ac6361db815f', 'https://www.qwiklabs.com/public_profiles/c297a75f-2f5e-4eed-9efc-3d528a3568dc', 'https://google.qwiklabs.com/public_profiles/44f798c8-43f4-4ef7-bd0e-68dba479d271', 'https://www.qwiklabs.com/public_profiles/df43e4b2-104f-403a-a218-ddb306535df7', 'https://google.qwiklabs.com/public_profiles/cfe70bc2-8595-47e2-a060-114d41f50fb1', 'https://google.qwiklabs.com/public_profiles/2a80151b-78b7-44a1-ab1c-8bd9af47f3cf', 'https://google.qwiklabs.com/public_profiles/2897ea58-6c22-4c90-9aa7-050c2cc54e6a', 'https://google.qwiklabs.com/public_profiles/1b6db191-edae-4f5d-81e3-2d2027f6f775', 'https://google.qwiklabs.com/public_profiles/0fdcbba2-c060-4072-996c-2cc7029ab44c', 'https://google.qwiklabs.com/public_profiles/7c821c73-0069-4a00-84ce-be5717aebd80', 'https://www.qwiklabs.com/public_profiles/25e8e649-86a4-41b7-acdd-e8946e31e2d3', 'https://google.qwiklabs.com/public_profiles/77218e9c-f3b0-47ee-90cc-1a6f5e950546', 'https://www.qwiklabs.com/public_profiles/62021504-b35f-427f-abae-07c175731422', 'https://www.qwiklabs.com/public_profiles/9487dc6c-8281-4547-8eda-df2bd31ec2b0', 'https://www.qwiklabs.com/public_profiles/29712c96-66b1-4656-941a-0ce5addc4920', 'https://google.qwiklabs.com/public_profiles/024877ea-1544-47ce-bfd1-d14c611e48e3', 'https://google.qwiklabs.com/public_profiles/c9190b32-90cc-46cb-9a17-317a095f9843', 'https://google.qwiklabs.com/public_profiles/f6e7fef4-1f70-453d-bace-6e5fe62a25a6', 'https://www.qwiklabs.com/public_profiles/addd8f36-06b9-475e-bd8f-10dff96af6aa', 'https://www.qwiklabs.com/public_profiles/ba97643b-d079-4732-bf37-d18464e1b645', 'https://www.qwiklabs.com/public_profiles/795e3843-aa0c-4c69-a4df-e4c3fafa8011', 'https://google.qwiklabs.com/public_profiles/e22ab44b-1690-4aac-a73e-cb253a1b071d', 'https://google.qwiklabs.com/public_profiles/a97b7f9b-95ac-402c-b09a-f363569d0543', 'https://www.qwiklabs.com/public_profiles/9e9706eb-067c-4ae3-a9d1-c5632a4096a8', 'https://www.qwiklabs.com/public_profiles/18987658-58d2-4d3d-b5e0-a17e976f644b', 'https://www.qwiklabs.com/public_profiles/a0aec15a-9c2a-458f-ab72-bbd6e572f58f', 'https://www.qwiklabs.com/public_profiles/a6ae06e5-ca6c-401f-b134-5ecc3ad3ede4', 'https://www.qwiklabs.com/public_profiles/ff9d504e-4c62-46cd-81cf-d372303b0ff2', 'https://google.qwiklabs.com/public_profiles/cde06b31-9b85-4ada-8ae2-416c067c72ae', 'https://google.qwiklabs.com/public_profiles/c3879a2c-0561-48d9-bf88-69c002c097d8', 'https://www.qwiklabs.com/public_profiles/98e9a09e-0e97-404c-ab94-9dda9a268c67', 'https://google.qwiklabs.com/public_profiles/0ec6b8f4-817c-4e38-9dc5-0dcbaeb220de', 'https://www.qwiklabs.com/public_profiles/687fa294-bc00-4a43-92dc-1f027624a2aa', 'https://google.qwiklabs.com/public_profiles/36e83809-6027-4777-ac98-5c902800e95d', 'https://google.qwiklabs.com/public_profiles/f24e30c4-b66e-4efd-baae-d1d6c2b2b0ac', 'https://google.qwiklabs.com/public_profiles/dba5fa2d-a14b-4b87-80ae-dff178af6d40', 'https://google.qwiklabs.com/public_profiles/e852198c-c129-4bb6-a085-854652a7ed16', 'https://google.qwiklabs.com/public_profiles/36bc21c7-2263-4564-ab5a-abbdfca62a81', 'https://www.qwiklabs.com/public_profiles/dfce1a20-1df5-41e0-b7eb-e42efa8553a1', 'https://www.qwiklabs.com/public_profiles/94ed4498-08fa-4eb3-b62e-ba6f0dc5d162', 'https://www.qwiklabs.com/public_profiles/e846dc79-30be-4dcc-be58-cad3beb4a6bc', 'https://www.qwiklabs.com/public_profiles/9c669717-104a-47ed-a925-a007a78da805', 'https://www.qwiklabs.com/public_profiles/49bdf2c2-aee6-4476-9d74-72227c1aaaf6', 'https://google.qwiklabs.com/public_profiles/50169ccc-1880-4788-8867-47f7e98cb218', 'https://google.qwiklabs.com/public_profiles/348ad4eb-2e97-4df2-b1d7-b4381cabe35a', 'https://www.qwiklabs.com/public_profiles/b098ae3c-303f-428b-a629-f18def22f6e3', 'https://google.qwiklabs.com/public_profiles/32b84358-9393-41a1-8705-29360bdb4105', 'https://google.qwiklabs.com/public_profiles/64ac6532-b69f-4e60-8e0a-8fae1e200406', 'https://google.qwiklabs.com/public_profiles/de0f837f-879d-4c2a-9f11-7dfd562c215f', 'https://www.qwiklabs.com/public_profiles/664b0059-7f97-4213-91f7-84e5d63958c6', 'https://www.qwiklabs.com/public_profiles/68cf7c4d-2ede-400b-8fed-60376e77f8e4', 'https://www.qwiklabs.com/public_profiles/0713b9b2-3fbb-4d3d-82ba-0207721abe23', 'https://google.qwiklabs.com/public_profiles/35fa1606-2e07-426f-968e-e02c650184ee', 'https://google.qwiklabs.com/public_profiles/efd1b99f-54ea-4133-8276-ce4374481dc0', 'https://google.qwiklabs.com/public_profiles/4232374e-01b8-4e05-8a28-4f6d93869b26', 'https://google.qwiklabs.com/public_profiles/4a908b3f-b7fd-496c-9314-44e2dc30b8b4', 'https://www.qwiklabs.com/public_profiles/36c3d86e-4d5f-42d3-ab70-74febe21ead1', 'https://www.qwiklabs.com/public_profiles/481f32c2-cf80-4059-959f-255d75e9b9a6', 'https://google.qwiklabs.com/public_profiles/1c7a19a7-7c25-4ab0-8200-800c0bc6b71c', 'https://google.qwiklabs.com/public_profiles/e3dc24ab-6494-44d2-9d4b-9c62e55357ba', 'https://google.qwiklabs.com/public_profiles/ddea7695-0953-4420-a575-a9e066b521e0', 'https://www.qwiklabs.com/public_profiles/3b9fa07e-c59e-44f1-b538-3d876c1e0c98', 'https://google.qwiklabs.com/public_profiles/ec1b45ea-610a-4fb9-8bea-af7e2c761afa', 'https://google.qwiklabs.com/public_profiles/95cccd1a-e6d3-4612-83e3-c5c616359281', 'https://google.qwiklabs.com/public_profiles/b7f6a20a-17b2-4c2b-b70d-eaac5d0dbcd2', 'https://www.qwiklabs.com/public_profiles/b362c6dc-9258-4cba-9d97-d9b5af352fc0', 'https://www.qwiklabs.com/public_profiles/6089ee97-e445-4c11-8839-2bb4448265b6', 'https://www.qwiklabs.com/public_profiles/d007fea7-bb7d-4417-b364-94fe6a60a2d5', 'https://www.qwiklabs.com/public_profiles/ffae7228-08e1-44b2-a2a5-0e27bf609f09', 'https://www.qwiklabs.com/public_profiles/db65fb90-431e-4f89-9348-b8f2a0ed8063', 'https://google.qwiklabs.com/public_profiles/11e39ffe-6081-47d3-86c9-d6f927159179']




track1=[
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

def data_scraping (url):
    start_thread(url)

def data_gathering(link):
    tempdic = {}
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    track1completed = []
    track2completed = []
    profile = soup.findAll('div', attrs = {'class':'public-profile__hero'})[0]
    dp = profile.img['src']
    name = profile.h1.text
    tlab = profile.p.text
    labsnum = tlab.split()
    tempdic['labsattempted'] = labsnum[0]
    tempdic['qlabid'] = link

    tempdic['id'] = len(biglist)+1
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
    tempdic['lentrack1'] = len(track1completed)
    tempdic['lentrack2'] = len(track2completed)
    #if tempdic['lentrack1'] == 6 or tempdic['lentrack2'] == 6:
    #id+=1
        #print(id)
    tempdic['qcomplete_no'] = len(track1completed) + len(track2completed)
    biglist.append(tempdic)
    if tempdic['qcomplete_no']!=0:
        print(tempdic['name']," got ",tempdic['qcomplete_no']," skill badges")

        #print("data saved")
    else:
    #    print(id,tempdic['name']," got ",tempdic['qcomplete_no']," skill badges")
        pass

def data_saving (biglist):
    #num = 0

    tk1 = 0
    tk2 = 0
    tkt = 0
    total_lab = 0
    for tempdic in biglist:
        if tempdic['qcomplete_no']!=0:
            smalllist.append(tempdic)

        x = int(tempdic['lentrack1'])
        y = int(tempdic['lentrack2'])
        z = int(tempdic['labsattempted'])
        if z>=35:
            total_lab+=1
            #if x<5 and y<6:
            #    print(tempdic['name'],"did",tempdic['labsattempted'], "and got",x,"in track 1 and",y,"in track 2")
        if x==6:
            tk1+=1
        if y==6:
            tk2+=1
        if x==6 or y==6:
            #print(tempdic['name'])
            tkt+=1


    print("Number of people completed track 1 : ",tk1)
    print("Number of people completed track 2 : ",tk2)
    print("Number of people completed atleast 1 track : ",tkt)
    print("Number of people may complete atleast 1 track  : ",total_lab)
    #print("number of people completed atleast one track ",num)
    #print(res)
    res = sorted(smalllist, key = lambda x: x['qcomplete_no'], reverse=True)
    print("number of people started : ",len(res))
    with open("my.json","w") as f:
        json.dump(res,f)
    f.close()


def start_thread(url2):
    threads = 5
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(data_gathering, url2)
    data_saving (biglist)

def main(url):
    data_scraping (url)

if __name__ == '__main__':
    t0 = time.time()
    #id = 0
    main(url)
    t1 = time.time()
    print(f"{t1-t0} seconds to download {len(url)} profile.")
    #print("number of people completed atleast one track",id)
