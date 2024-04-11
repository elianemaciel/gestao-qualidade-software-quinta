import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class TestContaBancaria {
    private ContaBancaria conta;

    @Before
    public void setUp() {
        conta = new ContaBancaria("Maria", 1000);
    }

    @Test
    public void testDeposito() {
        conta.depositar(500);
        assertEquals(1500, conta.getSaldo());
    }

    @Test
    public void testSaqueSucesso() {
        conta.sacar(500);
        assertEquals(500, conta.getSaldo());
    }

    @Test
    public void testSaqueSaldoInsuficiente() {
        conta.sacar(1500);
        assertEquals(1000, conta.getSaldo());
    }

    @Test
    public void testSaqueValorNegativo() {
        conta.sacar(-200);
        assertEquals(1000, conta.getSaldo());
    }

    @Test
    public void testDepositoValorNegativo() {
        conta.depositar(-200);
        assertEquals(1000, conta.getSaldo());
    }

    @Test
    public void testConsultarSaldo() {
        assertEquals(1000, conta.getSaldo());
    }
}
