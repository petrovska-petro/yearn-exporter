from brownie import chain
from yearn.networks import Network
from yearn.partners.snapshot import (BentoboxWrapper, DegenboxWrapper, Partner, WildcardWrapper,
                                     Wrapper, YApeSwapFactoryWrapper, GearboxWrapper)

partners = {
    Network.Mainnet: [
        Partner(
            name='tempus',
            treasury='0xab40a7e3cef4afb323ce23b6565012ac7c76bfef',
            wrappers=[
                Wrapper(
                    name='yvUSDC Tempus Pool',
                    vault='0xa354F35829Ae975e850e23e9615b11Da1B3dC4DE',
                    wrapper='0x443297DE16C074fDeE19d2C9eCF40fdE2f5F62C2',
                ),
                Wrapper(
                    name='yvDAI Tempus Pool',
                    vault='0xdA816459F1AB5631232FE5e97a05BBBb94970c95',
                    wrapper='0x7e0fc07280f47bac3D55815954e0f904c86f642E',
                )
            ]
        ),
        Partner(
            name='coinomo',
            treasury='0xd3877d9df3cb52006b7d932e8db4b36e22e89242',
            wrappers=[
                Wrapper(
                    name='yvUSDC',
                    vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                    wrapper='0xd3877d9df3cb52006b7d932e8db4b36e22e89242',
                ),
            ],
        ),
        Partner(
            name='alchemix',
            treasury='0x8392F6669292fA56123F71949B52d883aE57e225',
            wrappers=[
                Wrapper(
                    name='dai 0.3.0',
                    vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                    wrapper='0x014dE182c147f8663589d77eAdB109Bf86958f13',
                ),
                Wrapper(
                    name='dai 0.3.0 transmuter',
                    vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                    wrapper='0x491EAFC47D019B44e13Ef7cC649bbA51E15C61d7',
                ),
                Wrapper(
                    name='dai 0.4.3',
                    vault='0xdA816459F1AB5631232FE5e97a05BBBb94970c95',
                    wrapper='0xb039eA6153c827e59b620bDCd974F7bbFe68214A',
                ),
                Wrapper(
                    name='dai 0.4.3 transmuter',
                    vault='0xdA816459F1AB5631232FE5e97a05BBBb94970c95',
                    wrapper='0x6Fe02BE0EC79dCF582cBDB936D7037d2eB17F661',
                ),
                Wrapper(
                    name='weth 0.4.2',
                    vault='0xa258C4606Ca8206D8aA700cE2143D7db854D168c',
                    wrapper='0x546E6711032Ec744A7708D4b7b283A210a85B3BC',
                ),
                Wrapper(
                    name='weth 0.4.2 transmuter',
                    vault='0xa258C4606Ca8206D8aA700cE2143D7db854D168c',
                    wrapper='0x6d75657771256C7a8CB4d475fDf5047B70160132',
                ),
            ],
        ),
        Partner(
            name='inverse',
            treasury='0x926dF14a23BE491164dCF93f4c468A50ef659D5B',
            wrappers=[
                Wrapper(
                    name='dai-wbtc',
                    vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                    wrapper='0xB0B02c75Fc1D07d351C991EBf8B5F5b48F24F40B',
                ),
                Wrapper(
                    name='dai-yfi',
                    vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                    wrapper='0xbE21650b126b08c8b0FbC8356a8B291010ee901a',
                ),
                Wrapper(
                    name='dai-weth',
                    vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                    wrapper='0x57faa0dec960ed774674a45d61ecfe738eb32052',
                ),
                Wrapper(
                    name='usdc-weth',
                    vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                    wrapper='0x698c1d40574cd90f1920f61D347acCE60D3910af',
                ),
                Wrapper(
                    name='dola-stabilizer',
                    vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                    wrapper='0x973F509c695cffcF355787456923637FF8A34b29',
                ),
            ],
        ),
        Partner(
            name='frax',
            treasury='0x8d0C5D009b128315715388844196B85b41D9Ea30',
            wrappers=[
                Wrapper(
                    name='usdc',
                    vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                    wrapper='0xEE5825d5185a1D512706f9068E69146A54B6e076',
                ),
            ],
        ),
        Partner(
            name='pickle',
            treasury='0x066419EaEf5DE53cc5da0d8702b990c5bc7D1AB3',
            wrappers=[
                Wrapper(
                    name='usdc',
                    vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                    wrapper='0xEecEE2637c7328300846622c802B2a29e65f3919',
                ),
                Wrapper(
                    name='lusd',
                    vault='0x5fA5B62c8AF877CB37031e0a3B2f34A78e3C56A6',
                    wrapper='0x699cF8fE0C1A6948527cD4737454824c6E3828f1',
                ),
            ],
        ),
        Partner(
            name='badger',
            treasury='0xB65cef03b9B89f99517643226d76e286ee999e77',
            wrappers=[
                Wrapper(
                    name='wbtc',
                    vault='0xA696a63cc78DfFa1a63E9E50587C197387FF6C7E',
                    wrapper='0x4b92d19c11435614CD49Af1b589001b7c08cD4D5',
                ),
            ],
        ),
        Partner(
            name='deus',
            treasury='0x4e8a7c429192bfda8c9a1ef0f3b749d0f66657aa',
            wrappers=[
                Wrapper(
                    name='aeth',
                    vault='0x132d8D2C76Db3812403431fAcB00F3453Fc42125',
                    wrapper='0x4e8a7c429192bfda8c9a1ef0f3b749d0f66657aa',
                )
            ],
        ),
        Partner(
            name='basketdao',
            treasury='0x7301C46be73bB04847576b6Af107172bF5e8388e',
            wrappers=[
                WildcardWrapper(
                    name='bdi',
                    wrapper='0x0309c98B1bffA350bcb3F9fB9780970CA32a5060',
                ),
                WildcardWrapper(
                    name='bmi',
                    wrapper='0x0aC00355F80E289f53BF368C9Bdb70f5c114C44B',
                ),
            ],
        ),
        Partner(
            name='gb',
            treasury='0x6965292e29514e527df092659FB4638dc39e7248',
            wrappers=[
                WildcardWrapper(
                    name='gb1',
                    wrapper='0x6965292e29514e527df092659FB4638dc39e7248',
                ),
            ],
        ),
        Partner(
            name='donutapp',
            treasury='0x9eaCFF404BAC19195CbD131a4BeA880Abd09B35e',
            wrappers=[
                Wrapper(
                    name='yvDAI',
                    vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                    wrapper='0x9eaCFF404BAC19195CbD131a4BeA880Abd09B35e',
                ),
            ],
        ),
        Partner(
            name="yieldster",
            treasury='0x2955278aBCE187315D6d72B0d626f1217786DF60',
            wrappers=[
                WildcardWrapper(
                    name="liva-one",
                    wrapper="0x2747ce11793F7059567758cc35D34F63ceE8Ac00",
                ),
            ],
        ),
        Partner(
            name="akropolis",
            treasury='0xC5aF91F7D10dDe118992ecf536Ed227f276EC60D',
            wrappers=[
                WildcardWrapper(
                    name="vaults-savings-v2",
                    wrapper="0x6511D8686EB43Eac9D4852458435c1beC4D67bc6",
                ),
            ],
        ),
        Partner(
            name="Mover",
            treasury='0xf6A0307cb6aA05D7C19d080A0DA9B14eAB1050b7',
            wrappers=[
                Wrapper(
                    name="savings_yUSDCv2",
                    vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                    wrapper="0x541d78076352a884C8358a2ac3f36408b99a18dB",
                ),
            ],
        ),
        Partner(
            name='yapeswap',
            treasury='0x10DE513EE154BfA97f1c2841Cab91E8C389c7c72',
            wrappers=[
                YApeSwapFactoryWrapper(
                    'yapeswap', '0x46aDc1C052Fafd590F56C42e379d7d16622835a2'
                ),
            ],
        ),
        Partner(
            name='abracadabra',
            treasury='0xDF2C270f610Dc35d8fFDA5B453E74db5471E126B',
            # brownie run abracadabra_wrappers
            wrappers=[
                BentoboxWrapper(
                    name='yvCurve-IronBank',
                    vault='0x27b7b1ad7288079A66d12350c828D3C00A6F07d7',
                    wrapper='0xEBfDe87310dc22404d918058FAa4D56DC4E93f0A',
                ),
                BentoboxWrapper(
                    name='yvCurve-stETH',
                    vault='0xdCD90C7f6324cfa40d7169ef80b12031770B4325',
                    wrapper='0x0BCa8ebcB26502b013493Bf8fE53aA2B1ED401C1',
                ),
                BentoboxWrapper(
                    name='yvUSDC',
                    vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                    wrapper='0x6cbAFEE1FaB76cA5B5e144c43B3B50d42b7C8c8f',
                ),
                BentoboxWrapper(
                    name='yvUSDT',
                    vault='0x7Da96a3891Add058AdA2E826306D812C638D87a7',
                    wrapper='0x551a7CfF4de931F32893c928bBc3D25bF1Fc5147',
                ),
                BentoboxWrapper(
                    name='yvWETH',
                    vault='0xa258C4606Ca8206D8aA700cE2143D7db854D168c',
                    wrapper='0x920D9BD936Da4eAFb5E25c6bDC9f6CB528953F9f',
                ),
                BentoboxWrapper(
                    name='yvYFI',
                    vault='0xE14d13d8B3b85aF791b2AADD661cDBd5E6097Db1',
                    wrapper='0xFFbF4892822e0d552CFF317F65e1eE7b5D3d9aE6',
                ),
                BentoboxWrapper(
                    name='yvWETH',
                    vault='0xa9fE4601811213c340e850ea305481afF02f5b28',
                    wrapper='0x6Ff9061bB8f97d948942cEF376d98b51fA38B91f',
                ),
                DegenboxWrapper(
                    name='yvCurve-CVXETH',
                    vault='0x1635b506a88fBF428465Ad65d00e8d6B6E5846C3',
                    wrapper='0xf179fe36a36B32a4644587B8cdee7A23af98ed37',
                ),
                DegenboxWrapper(
                    name='yvDAI',
                    vault='0xdA816459F1AB5631232FE5e97a05BBBb94970c95',
                    wrapper='0x7Ce7D9ED62B9A6c5aCe1c6Ec9aeb115FA3064757',
                )
            ],
        ),
        Partner(
                name='chfry',
                treasury='0x3400985be0b41Ce9778823E9618074115f830799',
                wrappers=[
                    Wrapper(
                        name='USDT yVault',
                        vault='0x7Da96a3891Add058AdA2E826306D812C638D87a7',
                        wrapper='0x87e51ebF96eEB023eCc28536Ad0DBca83dEE0203',
                    ),
                    Wrapper(
                        name='DAI yVault',
                        vault='0xdA816459F1AB5631232FE5e97a05BBBb94970c95',
                        wrapper='0xd5F38f4F1e0c157dd1AE8Fd66EE2761A14eF7324',
                    ),
                    Wrapper(
                        name='USDC yVault',
                        vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                        wrapper='0x782bc9B1F11cDBa13aCb030cDab04f04FB667846',
                    ),
                ],
            ),
        Partner(
            name='ambire',
            treasury='0xa07D75aacEFd11b425AF7181958F0F85c312f143',
            wrappers=[
                WildcardWrapper(
                    name="batcher",
                    wrapper="0x460fad03099f67391d84c9cc0ea7aa2457969cea",
                ),
            ],
        ),
        Partner(
            name='shapeshiftdao',
            treasury='0x90A48D5CF7343B08dA12E067680B4C6dbfE551Be',
            wrappers=[
                WildcardWrapper(
                    name='ShapeShift DAO Router',
                    wrapper='0x6a1e73f12018D8e5f966ce794aa2921941feB17E',
                ),
            ],
        ),
        Partner(
            name='gearbox',
            treasury='0x7b065Fcb0760dF0CEA8CFd144e08554F3CeA73D1',
            wrappers=[            
                GearboxWrapper(
                    name='gearbox usdc v1',
                    vault='0xa354F35829Ae975e850e23e9615b11Da1B3dC4DE',
                    wrapper='0x444CD42BaEdDEB707eeD823f7177b9ABcC779C04',
                ),
                GearboxWrapper(
                    name='gearbox dai v1',
                    vault='0xdA816459F1AB5631232FE5e97a05BBBb94970c95',
                    wrapper='0x444CD42BaEdDEB707eeD823f7177b9ABcC779C04',
                ),                
            ],     
        ),         
        Partner(
            name='wido',
            treasury='0x5EF7F250f74d4F11A68054AE4e150705474a6D4a',
            wrappers=[
                WildcardWrapper(
                    name='dt',
                    wrapper='0x7Bbd6348db83C2fb3633Eebb70367E1AEc258764',
                ),
                WildcardWrapper(
                    name='st',
                    wrapper='0x926D47CBf3ED22872F8678d050e70b198bAE1559',
                ),
            ],
        ),
    ],
    Network.Fantom: [
        Partner(
            name='abracadabra',
            treasury='0xb4ad8B57Bd6963912c80FCbb6Baea99988543c1c',
            wrappers=[
                BentoboxWrapper(
                    name='yvFTM',
                    vault='0x0DEC85e74A92c52b7F708c4B10207D9560CEFaf0',
                    wrapper='0xed745b045f9495B8bfC7b58eeA8E0d0597884e12'
                )
            ]
        ),
        Partner(
            name='qidao',
            treasury='0x679016B3F8E98673f85c6F72567f22b58Aa15A54',
            wrappers=[
                Wrapper(
                    name='fantom',
                    vault='0x0dec85e74a92c52b7f708c4b10207d9560cefaf0',
                    wrapper='0x7efb260662a6fa95c1ce1092c53ca23733202798',
                ),
                Wrapper(
                    name='dai',
                    vault='0x637ec617c86d24e421328e6caea1d92114892439',
                    wrapper='0x682e473fca490b0adfa7efe94083c1e63f28f034',
                ),
            ]
        ),
        Partner(
            name='tempus',
            treasury='0x51252c520375C6A236Bb56DdF0C407A099B2EC0e',
            wrappers=[
                Wrapper(
                    name='yvUSDC Tempus Pool',
                    vault='0xEF0210eB96c7EB36AF8ed1c20306462764935607',
                    wrapper='0x943B73d3B7373de3e5Dd68f64dbf85E6F4f56c9E',
                ),
                Wrapper(
                    name='yvDAI Tempus Pool',
                    vault='0x637eC617c86D24E421328e6CAEa1d92114892439',
                    wrapper='0x9c0273E4abB665ce156422a75F5a81db3c264A23',
                ),
                Wrapper(
                    name='yvUSDT Tempus Pool',
                    vault='0x148c05caf1Bb09B5670f00D511718f733C54bC4c',
                    wrapper='0xE9b557f9766Fb20651E3685374cd1DF6f977d36B',
                ),
                Wrapper(
                    name='yvWETH Tempus Pool',
                    vault='0xCe2Fc0bDc18BD6a4d9A725791A3DEe33F3a23BB7',
                    wrapper='0xA9C549aeFa21ee6e79bEFCe91fa0E16a9C7d585a',
                ),
                Wrapper(
                    name='yvYFI Tempus Pool',
                    vault='0x2C850cceD00ce2b14AA9D658b7Cad5dF659493Db',
                    wrapper='0xAE7E5242eb52e8a592605eE408268091cC8794b8',
                )
            ]
        ),
        Partner(
            name='Sturdy',
            treasury='0xFd1D36995d76c0F75bbe4637C84C06E4A68bBB3a',
            wrappers=[
                Wrapper(
                    name='yvWFTM',
                    vault='0x0DEC85e74A92c52b7F708c4B10207D9560CEFaf0',
                    wrapper='0x7d939674451ab005EC51d523f5D6846B745e2565',
                ),
                Wrapper(
                    name='yvBOO',
                    vault='0x0fBbf9848D969776a5Eb842EdAfAf29ef4467698',
                    wrapper='0x6C5ee1f9B050E0De3489d60f687bEf16ee5c4C3D',
                ),
                Wrapper(
                    name='yvfBEETS',
                    vault='0x1e2fe8074a5ce1Bb7394856B0C618E75D823B93b',
                    wrapper='0x63F925C970ba617662fde778Cf5fB70d798B2bB8',
                ),
                Wrapper(
                    name='yvLINK',
                    vault='0xf2d323621785A066E64282d2B407eAc79cC04966',
                    wrapper='0x197dcF678163C20d0D34dC8065F6eba36D5BAD3E',
                ),
            ],
        ),
        Partner(
            name='wido',
            treasury='0x5EF7F250f74d4F11A68054AE4e150705474a6D4a',
            wrappers=[
                WildcardWrapper(
                    name='Router',
                    wrapper='0x7Bbd6348db83C2fb3633Eebb70367E1AEc258764',
                ),
            ],
        ),
        Partner(
            name='beethovenx',
            treasury='0xa1E849B1d6c2Fd31c63EEf7822e9E0632411ada7',
            wrappers=[
                WildcardWrapper(
                    name='Vault',
                    wrapper='0x20dd72Ed959b6147912C2e529F0a0C651c33c9ce',
                ),
            ],
        ),
    ],
}.get(chain.id, [])
