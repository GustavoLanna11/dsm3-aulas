<?php
    require_once 'C:\xampp\htdocs\firebase\vendor/autoload.php';
    use Kreait\Firebase\Factory;

    class FirebaseCRUD{
        private $database;

        public function __construct(){
            $firebase=(new Factory)
            ->withServiceAccount(__DIR__.'/assets/config/chave-privada-firebase-biblioteca.json')
            
            //URL diretamente do firebase 
            ->withDataBaseUri('https://biblioteca-dsm3-858cb-default-rtdb.firebaseio.com/')
            ->createDataBase();

            //Inicializar a conexão com o Realtime database
            $this->database = $firebase;
        }

        //Inserir dados (Create)
        public function create($livro){
            $ref = $this->database->getReference('livros');
            $ref->push($livro);
            echo "ok";
        }

        //Consultar todos os documentos(Read)
        public function read(){
            $ref = $this->database->getReference('livros');
            $livros = $ref->getValue();
        }

        //Atualizar um documento (Update)
        public function update($id,$livros){
            $ref=$this->database->getReference('livros');
            $ref->set($livro);
        }

        //Excluir um documento (delete)
        public function delete($id){
            $ref = $this->database->getReference('livros/' .$id);
            $ref->remove();
        }
    }

    $firebaseCrud = new FireBaseCRUD();

    //Inserir dado
    $firebaseCrud->create([
        'titulo'=>'1984',
        'autor'=>'George orwell',
        'ano'=>1949,
        'genero' => 'Distopia'
    ]);
?>

