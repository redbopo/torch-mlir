import torch

from torch_mlir_e2e_test.torchscript.framework import TestUtils
from torch_mlir_e2e_test.torchscript.registry import register_test_case
from torch_mlir_e2e_test.torchscript.annotations import annotate_args, export

# ==============================================================================

class UniformModule(torch.nn.Module):

    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
    ])
    def forward(self, x, y, z):
        a = torch.ops.aten.uniform_(x, 1.0, 10.0)
        b = torch.ops.aten.uniform_(y, -20.0, -5.0)
        c = torch.ops.aten.uniform_(z, -15.0, 3.0)
        std = torch.cat([
            torch.flatten(torch.std(a)),
            torch.flatten(torch.std(b)),
            torch.flatten(torch.std(c))
        ])
        mean = torch.cat([
            torch.flatten(torch.mean(a)),
            torch.flatten(torch.mean(b)),
            torch.flatten(torch.mean(c))
        ])
        return std, mean


@register_test_case(module_factory=lambda: UniformModule())
def UniformModule_basic(module, tu: TestUtils):
    module.forward(
        tu.rand(256, 512, 8).double(),
        tu.rand(512, 1024, 4).double(),
        tu.rand(512, 256, 4).double())

# ==============================================================================

class UniformStaticModule(torch.nn.Module):

    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([256, 512, 8], torch.float64, True),
        ([512, 1024, 4], torch.float64, True),
        ([512, 256, 4], torch.float64, True),
    ])
    def forward(self, x, y, z):
        a = torch.ops.aten.uniform_(x, 1.0, 10.0)
        b = torch.ops.aten.uniform_(y, -20.0, -5.0)
        c = torch.ops.aten.uniform_(z, -15.0, 3.0)
        std = torch.cat([
            torch.flatten(torch.std(a)),
            torch.flatten(torch.std(b)),
            torch.flatten(torch.std(c))
        ])
        mean = torch.cat([
            torch.flatten(torch.mean(a)),
            torch.flatten(torch.mean(b)),
            torch.flatten(torch.mean(c))
        ])
        return std, mean


@register_test_case(module_factory=lambda: UniformStaticModule())
def UniformStaticModule_basic(module, tu: TestUtils):
    module.forward(
        tu.rand(256, 512, 8).double(),
        tu.rand(512, 1024, 4).double(),
        tu.rand(512, 256, 4).double())

# ==============================================================================

class BernoulliModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
    ])
    def forward(self, x, y, z):
        a = torch.bernoulli(x)
        b = torch.bernoulli(y)
        c = torch.bernoulli(z)
        mean = torch.cat([
            torch.flatten(torch.mean(a)),
            torch.flatten(torch.mean(b)),
            torch.flatten(torch.mean(c))
        ])
        std = torch.cat([
            torch.flatten(torch.std(a)),
            torch.flatten(torch.std(b)),
            torch.flatten(torch.std(c))
        ])
        return  mean, std


@register_test_case(module_factory=lambda: BernoulliModule())
def BernoulliModule_basic(module, tu: TestUtils):
    module.forward(
        tu.rand(256, 512, 8).double(),
        tu.rand(512, 1024, 4).double(),
        tu.rand(512, 256, 4).double())

# ==============================================================================

class BernoulliZerosModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([-1, -1], torch.float64, True),
    ])
    def forward(self, x):
        return torch.bernoulli(x)


@register_test_case(module_factory=lambda: BernoulliZerosModule())
def BernoulliZerosModule_basic(module, tu: TestUtils):
    module.forward(torch.zeros(4, 8).double())

# ==============================================================================

class BernoulliOnesModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([-1, -1], torch.float64, True),
    ])
    def forward(self, x):
        return torch.bernoulli(x)


@register_test_case(module_factory=lambda: BernoulliOnesModule())
def BernoulliOnesModule_basic(module, tu: TestUtils):
    module.forward(torch.ones(4, 8).double())

# ==============================================================================

class BernoulliFloatModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
    ])
    def forward(self, x, y, z):
        a = torch.ops.aten.bernoulli_(x, 0.4)
        b = torch.ops.aten.bernoulli_(y, 0.7)
        c = torch.ops.aten.bernoulli_(z, 0.5)
        mean = torch.cat([
            torch.flatten(torch.mean(a)),
            torch.flatten(torch.mean(b)),
            torch.flatten(torch.mean(c))
        ])
        std = torch.cat([
            torch.flatten(torch.std(a)),
            torch.flatten(torch.std(b)),
            torch.flatten(torch.std(c))
        ])
        return  mean, std


@register_test_case(module_factory=lambda: BernoulliFloatModule())
def BernoulliFloatModule_basic(module, tu: TestUtils):
    module.forward(
        tu.rand(256, 512, 8).double(),
        tu.rand(512, 1024, 4).double(),
        tu.rand(512, 256, 4).double())

# ==============================================================================

class BernoulliTensorModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
        ([-1, -1, -1], torch.float64, True),
    ])
    def forward(self, x, px, y, py, z, pz):
        a = torch.ops.aten.bernoulli_(x, px)
        b = torch.ops.aten.bernoulli_(y, py)
        c = torch.ops.aten.bernoulli_(z, pz)
        mean = torch.cat([
            torch.flatten(torch.mean(a)),
            torch.flatten(torch.mean(b)),
            torch.flatten(torch.mean(c))
        ])
        std = torch.cat([
            torch.flatten(torch.std(a)),
            torch.flatten(torch.std(b)),
            torch.flatten(torch.std(c))
        ])
        return  mean, std


@register_test_case(module_factory=lambda: BernoulliTensorModule())
def BernoulliTensorModule_basic(module, tu: TestUtils):
    module.forward(
        tu.rand(512, 512, 8).double(),
        tu.rand(512, 512, 8).double(),
        tu.rand(512, 1024, 4).double(),
        tu.rand(512, 1024, 4).double(),
        tu.rand(512, 256, 4).double(),
        tu.rand(512, 256, 4).double())
