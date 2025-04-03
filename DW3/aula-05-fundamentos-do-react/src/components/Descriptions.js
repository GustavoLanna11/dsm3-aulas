const Descriptions = (props) => {
    //props = {} é um objeto
    // props -> propriedades, forma de tirar o valor de um componente e jogar em outro
    return(
        <>
            <div>
                <p>Seu nome é: {props.name}</p>
                <p>Sua idade é: {props.age}</p>
            </div>
        </>
    );
};

export default Descriptions;