from config import Config
from pathlib import Path
from copy import deepcopy
import json

conf = Config.from_json_file(Path("gen_config.json"))

data = {}
dicts = []
for epoch_count in conf.epochs:
    data['EPOCHS'] = epoch_count

    for batch_size in conf.batch:
        data['BATCH_SIZE'] = batch_size

        for hidden_layers in conf.layers:
            data['LAYERS'] = hidden_layers
            data['IN_DIM'] = 900

            for num_nodes in conf.nodes:
                data['NUM_NODES'] = num_nodes

                for latents in conf.latent:
                    data['LATENT'] = latents

                    for activate in conf.activation:
                        data['ACTIVATE'] = activate
                        dicts.append(deepcopy(data))

conf_list = []
for i in range(len(dicts)):
    outname = "config_E" + str(dicts[i]["EPOCHS"]) + "_B" + str(dicts[i]["BATCH_SIZE"]) + "_D" + str(dicts[i]["LAYERS"]) + "_N" + str(dicts[i]["NUM_NODES"]) + "_L" + str(dicts[i]["LATENT"]) + "_" + dicts[i]["ACTIVATE"] + ".json"
    conf_list.append(deepcopy(outname))
    with open("configs/" + outname, 'w') as outfile:
        json.dump(dicts[i], outfile)

commfile = open("hpo_commands", "w")
for i in range(len(conf_list)):
    commfile.write("python pytorch_vae.py " + conf_list[i] + '\n')






                    
                    
