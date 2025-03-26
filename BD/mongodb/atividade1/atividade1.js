// Importando o módulo do mongoClient
const {MongoClient} = require('mongodb');

//Criação da função principal
async function main(){
    //Definindo a conexão com o mongo
    const uri = "mongodb://127.0.0.1:27017";
    //criando instância do cliente
    const client = new MongoClient(uri);

    try {
        //Conectando com o servidor 
        await client.connect();
        //1 - selecionando o banco
        const database = client.db('zoo_db');
        //selecionando a coleção animais
        const animais = database.collection('animais');

        //2 - inserindo as informações no nosso banco
        await animais.insertMany([
            {nome: "Thor", especie: "Tigre-de-bengala", idade: 20, dieta: "Carnívoro", habitat: "Floresta Tropical", vacinado: false },
            {nome: "Luna", especie: "Arara-azul", idade: 10, dieta: "Herbívoro", habitat: "Deserto", vacinado: false },
            {nome: "Feroz", especie: "Leão", idade: 5, dieta: "Carnívoro", habitat: "Floresta Tropical", vacinado: false },
            {nome: "Víbora", especie: "Naja", idade: 2, dieta: "Carnívoro", habitat: "Deserto", vacinado: false },
            {nome: "Luther", especie: "Jaguar", idade: 3, dieta: "Carnívoro", habitat: "Floresta Tropical", vacinado: false },
        ])

        //3 - Consultando todos os animais
        const todosAnimais = await animais.find().toArray();
        console.log('Animais:', todosAnimais);

        // 3 - consultando animais do deserto
        const animaisDeserto = await animais.find({habitat: "Deserto"}).toArray();
        console.log('Animais do Deserto: ', animaisDeserto);

        // 4 - Atualizando os animais felinos como vacinados
        await animais.updateMany(
            {nome: { $in: ["Thor", "Feroz", "Luther"] } }, //Filtro para encontrar animais
            {$set: {vacinado:true}} //Valor atualizado para o campo em específico
        );

        //Consultando itens pós alteração
        const updatedAnimais = await animais.find().toArray();
        console.log('Animais Atualizados: ', updatedAnimais);

        //5 - limpeza dos registros (animal > 15 anos)
        await animais.deleteMany({ idade: { $gt: 15}});

        //6 - adicionando o campo cuidador (responsável por todos) no zoológico
        await animais.updateMany(
            {}, 
            { $set: { cuidador: "Gustavo" } }  
          );

    } finally{
        await client.close();
    }
}

// Chama a função principal e captura o erro, se houver
main().catch(console.error);