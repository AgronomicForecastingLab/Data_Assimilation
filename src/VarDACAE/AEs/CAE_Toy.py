
from VarDACAE.AEs import BaseAE
from VarDACAE.AEs import Jacobian

class ToyCAE(BaseAE):
    """Creates a simple CAE for which
    I have worked out the explicit differential
    """
    def __init__(self, input_size, latent_dim, activation, hidden):
        if activation == "lrelu":
            raise NotImpelemtedError("Leaky ReLU not implemented for ToyAE")
        super(ToyCAE, self).__init__()


    def jac_explicit(self, x):
        """Generate explicit gradient for decoder
        (from hand calculated expression)"""

        # use Jacobian.accumulated_slow() for now
        raise NotImpelemtedError()

